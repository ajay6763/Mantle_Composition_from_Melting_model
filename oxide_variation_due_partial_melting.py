
# Script to calculate chemical variation of  solid and melt phases due to
# partial melting based on Langmuir et al.,1992 fromAfons,s G3 LitMod paper

# read the database percentage of oxides in source (solid) and bulk
# partition coefficient of oxides

import numpy as np
import matplotlib.pyplot as plt





rho_crust=2950;# density of oceanic crust in kg/m3
g=9.8;# accelration due to gravity
## Po and Pf are dependent on the composition fugacity oxygen, or presence of wa
#ter.
# standard values can be used or can be computed (e.g pmelts need to know how to)
Po=2.75; # pressure at intersection of solidus. Essensially pressure at which me
#lting starts (P in GPa)
Pf=0.2;# pressure at which melting stops (P in GPa)
# these values of Po and Pf are from Asimow et al.,1999,2001 
##
hc=6.0# thickness of oceanic crust

## Calculating mean fractional melting
F_mean= (hc*rho_crust*g)/((Po-Pf)*10**4)/100; # Based on Afonso,s G3 paper about LitMod
F_mean=0.06
print("Mean partial fractionation:",F_mean)
#                SiO2  Al2O3   MgO    Fe0    CaO   Na2O
#PUM Hart and Zindler(1986)
PUM_J_x_s_o= np.array([45.20, 4.00, 38.30, 7.80,  3.50,  0.36]); # initial concentration of oxides in the original source (wt%)
PUM_MS_x_s_o=np.array([45.00, 4.50, 37.80, 8.10,  3.60,  0.33]); # initial concentration of oxides in the original source (wt%)
DMM_x_s_o=   np.array([44.71, 3.98, 38.73, 8.18,  3.17,  0.13]);
#x_s_o=DMM_x_s_o # np.array([44.71,  3.98,  38.73, 8.12,  3.17,  0.12]);
bulk_D=np.array([]) # bulk distrubution coeficient
x_s_resi=np.array([])# concentration of oxides in the solid after partial melting (wt%)
x_l_computed=np.array([]) # concentration of oxides in the liquid (wt%)
x_l_calc=np.array([]) # concentration of oxides in the liquid (wt%)

#F_mean=10#mean fractional melting

## variation presure form Po Pf
P=((0.2*10**9)*10**-5)/1000; # Pressure in kilobars
# Bulk Partition Coefficients for major oxides Niu(1997)
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

# doding the fractionation based on Langmuir et al.,1992

x_s_resi= DMM_x_s_o/((F_mean/bulk_D) + (1-F_mean))
x_l_computed = DMM_x_s_o- x_s_resi	
x_l_calc = DMM_x_s_o/bulk_D 
print(DMM_x_s_o)
print("Bulk D",bulk_D)
print("residual in the solid",x_s_resi)
print("in liquid calculated",x_l_calc)
print("in liquid computed",x_l_computed)
print(x_l_computed[:]==x_l_calc[:])
##plotting
plt.grid(color='grey', linestyle='-', linewidth=1)
plt.plot(np.array(x_s_resi),color="red",lw=1,marker='o',label='Calculated')
plt.plot(np.array(PUM_MS_x_s_o),color="blue",lw=1,marker='o',label='PUM')
plt.plot(np.array(DMM_x_s_o),color="black",lw=1,marker='o',label='DMM')

plt.xticks([-1,0, 1, 2, 3,4,5,6],[" ","SiO2","Al2O3","MgO","FeO","CaO","Na2O"])
plt.xlabel('Major oxides ')
plt.legend()
plt.ylabel('(wt %)')


plt.show()

