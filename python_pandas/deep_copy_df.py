import pandas as pd
file_path = 'https://github.com/sandiprathore/python-practice/files/8253144/data.csv'
original_dataframe = pd.read_csv(file_path,  sep='|')
dataframe_copy = original_dataframe.copy(deep=True)
print(original_dataframe)
print(dataframe_copy)