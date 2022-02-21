# Python Program for Sum the digits of a given number

number = input("Enter a number: ")
sum_of_digits = 0 
for num in number:
    num = int(num)
    sum_of_digits = sum_of_digits + num
print(f'The of all digits in {number} is {sum_of_digits}')