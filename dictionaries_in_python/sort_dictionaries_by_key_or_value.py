# dictionary
dic = {"coconut": 5, "banana": 2, "apple": 3}

# sort by keys
sorted_dic_by_keys = dict(sorted(dic.items()))
print("sorted dictionary by keys",sorted_dic_by_keys)

# sort by values 
sorted_dic_by_values = dict(sorted(dic.items(), key=lambda item: item[1]))
print("sorted by values ",sorted_dic_by_values) 