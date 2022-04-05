test_dict = {'name' : ["sarita", "bharti", "kiran"], 'age' : [17, 16, 18]}
result_list = []
for key, val in test_dict.items():
    result_list.append([key] + val)
print(result_list)