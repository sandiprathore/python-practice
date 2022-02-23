# Python program to print odd numbers in a list
test_list = [2, 7, 5, 64, 14]
odd_numbers = []
for element in test_list:
    if element%2 !=0:
        odd_numbers.append(element)
print(f"Odd numbers in given list: {odd_numbers}")