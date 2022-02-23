# Python program to remove empty tuples from a list

test_list = [(), ('ram','15','8'), (), ('laxman', 'sita'),('krishna', 'akbar', '45'), ('',''),(),[]]
updated_list = []
for ele in test_list:
    if len(ele) >0 :
        updated_list.append(ele)
print(F"None emty tuple list is :{updated_list}")