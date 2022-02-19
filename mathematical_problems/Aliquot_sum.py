# Program to get aliquot sum  
number=int(input("enter a number: "))
i = 1
Aliquot_sum = 0
while i<number:
    if number % i == 0:
        Aliquot_sum = Aliquot_sum + i
    i=i+1
print(f'The Aliquot sum of {number} is {Aliquot_sum}')