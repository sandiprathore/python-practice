import pandas as pd
s = [
    ['sandip', ['b.tech','IPS','IPS'], '21'],
    ['atul', ['b.tech','b.tech'],'45'],
    ['kajal', ['BSC','b.tech','BSC'],'45']
    ]

columns = ['name','degree','age']
df = pd.DataFrame(s, columns=[columns])
m_df = df.to_markdown()
print(m_df)