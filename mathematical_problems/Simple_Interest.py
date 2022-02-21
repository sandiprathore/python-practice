# Python Program to calculate simple interest
principal_amount = float(input("Enter your principal amount: "))
rate_of_interest = float(input("Enter rate in '%': ")) 
time = float(input("Enter time duration in years: "))
simple_intrest = (principal_amount*rate_of_interest*time)/100
print(f"simple intrest of {principal_amount} rs for {time} year is {simple_intrest} rs with {rate_of_interest} % rate of interest.") 