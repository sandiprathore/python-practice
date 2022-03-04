import pandas as pd 
data_frame = pd.read_csv('data.csv', sep='|')
data_frame[["No_1", "No_2"]] = data_frame["Mo_no"].str.split(",", expand=True)
print(data_frame)