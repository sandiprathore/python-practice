number=int(input("Enter a number: "))
if number>1:
    for checking_variable in range(2,number):
        if (number%checking_variable)==0:
           
            print(number," is not prime number. It is divisible by ",checking_variable)
            break
    else:
        print(number," is prime number ")
else:
    print(number," is prime number")