import pandas as pd 
data_frame = pd.read_csv('data_2.csv')
data_frame.rename(columns={'No_1': 'phone_1', 'No_2': 'phone_2'}, inplace=True)
print(data_frame)










