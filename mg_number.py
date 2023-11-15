"""
The magnesium number (Mg number / Mg# = 100 × Mg/(Mg + Fe)), as a geochemical potential tracer, can indicates the depleted degree of mantle.

In other words, Mg# is a ratio of magnesium to iron in an igneous rock, which is related to the chemical composition of the mantle material. As the magma cools, lighter minerals solidify first, forming a scum on the surface of the molten rock. If the composition of the mantle is known, the magnesium number can be predicted, and the magnesium number provides information on the composition of the mantle rock. The magnesium number also provides information on the thermal history of the rock (https://www.oxfordreference.com/display/10.1093/oi/authority.20110803100125853). 


@author: wzhang
@e-mail: wzhang@geo3bcn.csic.es
@version: Python3.8
@time: 2023-11-13
"""


MgO = float(input('Enter MgO wt%: '))
ans = int(input('Do you have FeO--1 or Fe2O3--2 (choose 1 or 2 ):'))
FeO = float(input('Enter FeO wt%: '))

# The atomic weight of MgO and FeO
MgO_w=40.3044		# 24.305 + 15.9994 = 40.3044
FeO_w=71.8444 		# 55.845 + 15.9994 = 71.8444
Fe2O3_w=159.6882		# 55.845 * 2 + 15.9994 * 3 = 159.6882

if ans==1:
	mg_No= 100 * ((MgO/MgO_w)/((MgO/MgO_w)+(FeO/FeO_w)))
	print( 'Mg number FeO: ',mg_No) 

elif ans==2:
	## Need to conver Fe2O3 to Feo
	FeO= FeO * Fe2O3_w/FeO_w/2
	mg_No= 100 * ((MgO/MgO_w)/((MgO/MgO_w)+(FeO/FeO_w)))
	print( 'Mg number Fe2O3: ',mg_No) 
