# Python program to print positive and negative numbers in a list
test_list = [2, 7, -5, 64, -14]
positive_numbers = []
negative_numbers = []
for element in test_list:
    if element>=0:
        positive_numbers.append(element)
    else:
        negative_numbers.append(element)
print(f"Positive numbers in given list: {positive_numbers}")
print(f"Negative numbers in given list: {negative_numbers}")