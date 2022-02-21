starting_value  = int(input("Enter the starting value: "))
ending_value = int(input("Enter the ending value: "))
print("Enen numbers in range",starting_value ,"to",ending_value,"are: ")
while starting_value  <= ending_value:
    if (starting_value %2) != 0: 
        print(starting_value ,end=' ')
    starting_value =starting_value +1

