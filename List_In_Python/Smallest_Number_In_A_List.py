
# Python program to find smallest number in a list

# mathod 1
test_list = [ 1, 6, 3 ]
smallest_number_in_a_list = min(test_list)
print("smallest number in a list is: ",smallest_number_in_a_list)


# mathod 2

test_list = [ 4, 6, 3 ]
test_list.sort()
smallest_number = test_list[0] 
print("smallest number in a list is: ",smallest_number)
