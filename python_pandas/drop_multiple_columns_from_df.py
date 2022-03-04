# method 1 

import pandas as pd 
data_frame = pd.read_csv('data_2.csv')
data_frame.drop(['Mo_no','No_1'], axis=1, inplace=True)
print(data_frame)

# method 2

import pandas as pd 
data_frame_2 = pd.read_csv('data_2.csv')
df = data_frame_2.drop(columns=['Mo_no', 'No_1'])
print(df)