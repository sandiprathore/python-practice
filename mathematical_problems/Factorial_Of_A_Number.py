# Python Program for factorial of a number 

number = int(input("Enter a number: "))
factiorial = 1
for num in range(1,number+1):
    factiorial = factiorial * num
print(f'Factorial of {number} is {factiorial}') 
