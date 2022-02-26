# Python Program to Split the array and add the first part to the end
i=int(input("Enter index: "))
array = [12, 10, 5, 6, 52, 36]
slipted_list = array[i:] +  array[:i]
print(slipted_list)