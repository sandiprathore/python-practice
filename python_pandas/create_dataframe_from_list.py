import pandas as pd 
list_of_numbers = [1,2,3]
column_names = ["column"]

df = pd.DataFrame(list_of_numbers,columns=column_names)
print(df)