#take input from the user 
num_1=float(input("enter the first number: "))
num_2=float(input("enter the second number: 12"))
num_3=float(input("enter the thard number: "))
# conditions to check largest number
if num_1>num_2 and num_1>num_3:
    print( "ther largest number is: ",num_1)
elif num_2>num_1 and num_2>num_3:
    print("the largest number is: ",num_2)
else:
    print("the largest number is: ",num_3)
