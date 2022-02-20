# Python Program to check Armstrong Number

number = int(input("Enter a number: "))
temp_number = number
power = len(str(number))
s = 0
while number >0:
    num = (number%10) ** power
    s = s + num
    number=number//10
if temp_number == s:
    print(f'{temp_number} is armstrong number')
else:
    print(f'{temp_number} is not armstrong number')