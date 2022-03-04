# dictionary
dic = {"coconut": 5, "babu": 2, "amit": 3}

# Approach 1 
sum_of_all_values = 0 
for value in dic.values():
    sum_of_all_values = sum_of_all_values + value 
print(f'sum of all values: {sum_of_all_values}')

# Approach 2 
sum_of_all_values = 0 
for key in dic:
    sum_of_all_values = sum_of_all_values + dic[key]
print(f'sum of all values: {sum_of_all_values}')