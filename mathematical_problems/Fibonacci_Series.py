# Python program to print Fibonacci Series for given terms
first_term = 0
second_term = 1
number = int(input("Enter terms: "))
if number<0:
    print("Enter a positive number")
else: 
    print(f"Fibonacci Series for {number} terms")
    for num in range(1,number+1):
        print(first_term, end=' ')
        sum_of_two_terms = first_term  + second_term
        first_term  = second_term
        second_term=sum_of_two_terms