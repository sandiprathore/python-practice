# Python program to print all Prime numbers in given range

starting_number = int(input("Enter the starting number: "))
ending_number = int(input("Enter the ending number: "))
list_of_prime_num=[]
for num in range(starting_number,ending_number+1):
    for i in range (2,num):
        if (num%i) ==0:
            break
    else:
        list_of_prime_num.append(num)
print(f'List of prime number from {starting_number} to {ending_number} is {list_of_prime_num}')