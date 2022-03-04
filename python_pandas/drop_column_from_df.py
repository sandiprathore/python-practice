import pandas as pd 
data_frame_2 = pd.read_csv('data_2.csv')
data_frame_2.drop('Mo_no', axis=1, inplace=True)
print(data_frame_2)