starting_value = int(input("Enter a starting value: "))
temp_ver = starting_value
ending_value = int(input("Enter a ending value: "))
sum_of_even_num = 0
while starting_value <= ending_value :
    if starting_value %2 != 0:
        sum_of_even_num = sum_of_even_num + starting_value 
    starting_value = starting_value + 1
print(f'The sum of even numbers in range {temp_ver} to {ending_value} is {sum_of_even_num}')
