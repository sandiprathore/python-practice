# lsit of dictionaries
list_of_dic = [
    {"name":"raja", "age":42,"city":"indore"},
    {"name":"ramesh", "age":26,"city":"bhopal"},
    {"name":"suraj", "age":19,"city":"khandwa"}
]

# using function

def dic_function(key_of_dic):
    dic= (key_of_dic["age"])
    return dic
sorted_list_of_dic = sorted(list_of_dic, key=dic_function)
print(sorted_list_of_dic)


# Pthon program to sort list of dictionaries by values Using itemgetter
from operator import itemgetter
sorted_list_itm = sorted(list_of_dic, key=itemgetter('age')) 
print(sorted_list_itm)

# Pthon program to sort list of dictionaries by values Using lambda function 
sorted_list = sorted(list_of_dic, key = lambda sam: sam['age']) 
print(sorted_list)