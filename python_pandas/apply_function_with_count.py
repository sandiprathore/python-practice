import pandas as pd
data = [
    ['sandip', ['b.tech','IPS','IPS'], '21'],
    ['atul', ['b.tech','b.tech'],'45'],
    ['kajal', ['BSC','b.tech','BSC'],'45']
    ]

columns = ['name','degree','age']
df = pd.DataFrame(data, columns=[columns])

def degree_count(row: pd.Series)->tuple:
    count_of_btech = row['degree'].count('b.tech')
    count_of_bsc = row['degree'].count('BSC')
    count_of_ips = row['degree'].count('IPS')
     
    return count_of_btech, count_of_bsc, count_of_ips 

list_of_new_columns = [
    'count_of_btech', 
    'count_of_bsc',
    'count_of_ips' 
    ]
df[list_of_new_columns] = df.apply(degree_count,axis=1,result_type='expand')
print(df)