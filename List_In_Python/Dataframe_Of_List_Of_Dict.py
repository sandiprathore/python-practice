# dataframe of list of dictionaries 

import pandas as pd
lis = [{ "name" : "Nandini", "age" : 20}, 
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]
df = pd.DataFrame(lis)
print(df)