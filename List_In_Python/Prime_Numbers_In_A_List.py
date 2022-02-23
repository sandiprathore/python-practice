# Python program to print prime numbers in a list
test_list = [2, 7, 5, 64, 14,3,7]
prime_number = []
for element in test_list:
    for num in range(2,element):
        if element%num ==0:
            break
    else:
        prime_number.append(element)
print(f'Prime numbers in given list: {prime_number}')