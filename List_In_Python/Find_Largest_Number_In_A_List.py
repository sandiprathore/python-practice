
# Python program to find largest number in a list

# mathod 1
test_list = [ 1, 6, 3 ]
largest_number_in_a_list = max(test_list)
print("smallest number in a list is: ",largest_number_in_a_list)


# mathod 2

test_list = [ 4, 6, 3 ]
test_list.sort()
largest_number = test_list[-1] 
print("largest number in a list is: ",largest_number)
