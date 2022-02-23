# Python program to print even and odd numbers in a list
test_list = [2, 7, 5, 64, 14]
even_numbers = []
for element in test_list:
    if element%2 ==0:
        even_numbers.append(element)
print(f"Even numbers in given list: {even_numbers}")