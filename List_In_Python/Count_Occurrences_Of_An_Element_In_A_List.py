# Python Program to Count occurrences of an element in a list

from gettext import find


test_list = [1,2,8,3,5,1]

# method 1 
find_element = int(input("Enter number which you want to count: "))
count = 0 
for element in test_list:
    if find_element == element:
                   count = count + 1
print(f"{find_element} is {count} times in the list")


# method 2
count = test_list.count(find_element)
print(f"{find_element} is {count} times in the list")