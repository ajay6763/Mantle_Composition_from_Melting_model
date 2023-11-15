"""
To calculate chemical variation of  solid and melt phases due to partial melting based on Langmuir et al.,1992 from Afonso et al., 2008 G3 LitMod paper

F(P) = 25.23-16.19P when P > 1.25 
F(P) = 10.0-4.0P    when P < 1.25
where P is pressure, GPa; F(P) is degree of partial melting, non-dimension.

@author: wzhang
@e-mail: wzhang@geo3bcn.csic.es
@version: Python3.11
@time: 2023-11-13
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%% Reading
print("Reading composition file...")
df = pd.read_excel(r"Composition.xlsx")
figname = "Out.png"
# print(df)

print("\nReading the chemical composition of original source...")
x_o_name = "DMM"
print("The name of source (x_o, wt %): ", x_o_name)
for i in df.index:
	ann = df.loc[i]
	if ann['Name'] == x_o_name:
		print("# SiO2  Al2O3   MgO    Fe0    CaO   Na2O")
		x_o = np.array([ann['SiO2'], ann['Al2O3'],ann['MgO'],ann['TFeO'],ann['CaO'],ann['Na2O']])		
	if ann['Name'] == "PUM":
		print("# SiO2  Al2O3   MgO    Fe0    CaO   Na2O")
		PUM = np.array([ann['SiO2'], ann['Al2O3'],ann['MgO'],ann['TFeO'],ann['CaO'],ann['Na2O']])	
		
print(x_o)

#%% Calculating
F_mean=0.06    # mean fractional melting
print("\nMean partial fractionation:",F_mean)
P1 = (25.23-100*F_mean)/16.19
P2 = (10.0-100*F_mean)/4.0
print("P1,P2 (GPa) from Afonso et al., (2008):",P1,P2)

## variation presure form Po Pf
# P=((0.2*10**9)*10**-5)/1000; # Pressure in kilobars, GPa -> kilobar
# P=((1.5*10**9)*10**-5)/1000  # Pressure in kilobars why is 1.5 GPa
if F_mean>0.05:
	P = P1*10
else:
	P = P2*10

print("Calculating the pressure, kilobars:",P)

# Bulk Partition Coefficients for major oxides Niu(1997)
print("\nCalculating the major oxides of both residue and melt with Bulk Partition Coefficients from Niu(1997).")
bulk_D=np.array([]) # bulk distrubution coeficient
#         oxide      a         b         c       d
#SiO2
bulk_D=np.append(bulk_D,[0.8480 - (0.2200*F_mean)  +  (0.0055*P)])
#Al2O3
bulk_D=np.append(bulk_D,[0.1890 - (0.5100*F_mean)  -  ((2.5*10**-4)*F_mean**(-1))   +  0.0010*P])
#MgO
bulk_D=np.append(bulk_D,5.2000 - (7.5664*F_mean)  -  (0.0594*P))
#FeO
bulk_D=np.append(bulk_D,[0.3169 + (0.3695*F_mean)  -  ((3.4586*10**-3)*P)			  +  0.2130*bulk_D[2]])

#CaO
bulk_D=np.append(bulk_D,0.3180 - (1.2200*F_mean)  +  ((2.7200*10**-3)*(F_mean**-1))   +  0.0005*P)
#Na2O
bulk_D=np.append(bulk_D,0.0639 - (0.5787*F_mean)  +  (2.4763*(F_mean**2))		      -  3.6717*(F_mean**3))

# doing the fractionation based on Langmuir et al.,1992
x_s_resi= x_o/((F_mean/bulk_D) + (1-F_mean))
x_l_calc = x_s_resi/bulk_D 
print("Bulk Partition Coefficients from Niu(1997): ",bulk_D)
print("The chemical composition of Residue (solid), x_s: ",x_s_resi)
print("The chemical composition of melt (liquid), x_l:",x_l_calc)

#%% plotting
plt.figure()
plt.grid(color='grey', linestyle='-', linewidth=1)
plt.plot(np.array(PUM),color="blue",lw=1,marker='o',label='PUM')
plt.plot(np.array(x_o),color="black",lw=1,marker='o',label=x_o_name)
plt.plot(np.array(x_s_resi),color="red",lw=1,marker='o',label='Residue, F='+str(F_mean))
plt.plot(np.array(x_l_calc),color="red",lw=1,marker='s',label='Melt, F='+str(F_mean))

plt.xticks([0, 1, 2, 3,4,5],["SiO2","Al2O3","MgO","FeO","CaO","Na2O"])
plt.xlabel('Major oxides ')
plt.legend()
plt.ylabel('Weight percentage, wt %')

plt.savefig(figname)