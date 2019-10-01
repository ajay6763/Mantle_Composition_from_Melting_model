"""
to calculate total amount of partial melting given thickness of oceanic crust
Need to calculate total amout of oceanic crust which has been extracted since the start of the plate tectonics:
Assumptions:
1. assuming start of plate tectonics at 4.2 billons years ago (4200 ma)
2. cycles of 200 million years for oceanic crust formation 
3. assuming area of oceans is as that of present area (very loose assumtion need to think about this) = 361.9 millon square kilometers

Number of oceneanic crust production cycles 4200/200 = 21 

4. assuming average thickness of oceanic crust = 7.5km 

5. total volume of oceanic crust produced = oceanic are * thickness of oceanic crust
   361.9*1000000*7.5 = 2714250000 km




"""
rho_crust=2880;# density of oceanic crust in kg/m3
g=9.8;# accelration due to gravity
## Po and Pf are dependent on the composition fugacity oxygen, or presence of wa
#ter.
# standard values can be used or can be computed (e.g pmelts need to know how to)
Po=2.75; # pressure at intersection of solidus. Essensially pressure at which me
#lting starts (P in GPa)
Pf=0.2;# pressure at which melting stops (P in GPa)
# these values of Po and Pf are from Asimow et al.,1999,2001 
##
hc=8;#  2714250000;# thickness of oceanic crust

## Calculating mean fractional melting
F_mean= (hc*rho_crust*g)/((Po-Pf)*10**4); # Based on Afonso,s G3 paper about LitMod
print("Mean partial fractionation:",F_mean)