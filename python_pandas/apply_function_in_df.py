import pandas as pd 
# read csv file 
dataframe = pd.read_csv('aplly.csv')

# New columns that we want to add 
list_of_columns = ['multiple', 'subtraction', 'addition']

# function 
def operations( row: pd.Series) -> tuple:
    multiple = row['a']*row['b']
    subtraction = row['a'] - row['b']
    addition = row['a'] + row['b']
    return multiple, subtraction, addition

# apply function on df 
dataframe[list_of_columns]=dataframe.apply(operations,axis=1,result_type='expand')