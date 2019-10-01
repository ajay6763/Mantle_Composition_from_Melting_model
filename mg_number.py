
MgO =input('Enter MgO wt%: ')
FeO =input('Enter FeO wt%: ')

MgO_w=40.3044 
FeO_w=71.844
mg_No= ((MgO/MgO_w)/((MgO/MgO_w)+(FeO/FeO_w)))*100
print mg_No
