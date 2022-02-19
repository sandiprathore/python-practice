# Python Program to Find the Sum of Natural Numbers
starting_value = int(input("Enter a starting number: "))
tem_ver = starting_value
ending_value = int(input("Enter a ending number: "))
sum_of_natural_numberes=0
while starting_value <= ending_value:
    sum_of_natural_numberes = sum_of_natural_numberes+ starting_value
    starting_value = starting_value + 1
print(f'The sum of natura numberes in range {tem_ver} to {ending_value} is {sum_of_natural_numberes}')