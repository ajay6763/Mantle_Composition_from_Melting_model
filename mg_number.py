
MgO =input('Enter MgO wt%: ')
ans =input('Do you have FeO--1 or Fe2O3--2 (choose 1 or 2 ):')
FeO =input('Enter FeO wt%: ')
MgO_w=40.3044 
FeO_w=71.844 

if ans==1:
	mg_No= ((MgO/MgO_w)/((MgO/MgO_w)+(FeO/FeO_w)))*100
	print( 'Mg number FeO',mg_No) 

elif ans==2:
	## Need to conver Fe2O3 to Feo
	FeO= FeO*0.8998
	mg_No= ((MgO/MgO_w)/((MgO/MgO_w)+(FeO/FeO_w)))*100
	print( 'Mg number Fe2O3',mg_No) 
