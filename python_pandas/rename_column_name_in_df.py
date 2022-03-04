import pandas as pd 
list_of_number = [1,2,3]
column_names = ["column"]
df = pd.DataFrame(list_of_number,columns=column_names)
df.rename(columns = {'column':'number'},inplace=True)