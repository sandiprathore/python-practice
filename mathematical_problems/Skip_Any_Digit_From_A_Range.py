number_1 = int(input("Enter the starting number: "))
number_2 = int(input("Enter the ending number: "))
skip_number = int(input("Enter the digit which you want to skip: "))
while number_1<=number_2:
    if number_1%10 == skip_number:
        number_1 = number_1 + 1
        continue
    else:
        print(number_1)
    number_1=number_1+1
