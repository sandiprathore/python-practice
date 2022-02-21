starting_value = int(input("Enter a starting value: "))
ending_value = int(input("Enter a ending value: "))
temp_ver = starting_value 
sum=0
while starting_value<=ending_value:
    sum=sum+starting_value*starting_value
    starting_value=starting_value+1
print( f'The sum of suquare in range {temp_ver} to {ending_value} is {sum}')