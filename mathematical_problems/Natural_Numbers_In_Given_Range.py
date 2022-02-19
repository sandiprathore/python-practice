# Python Program to Print Natural Numbers
starting_value =int(input("Enter the starting value: "))
ending_value =int(input("Enter the ending value: "))
print(f'Natural numbers from {starting_value } to {ending_value } are: ')
while starting_value <=ending_value :
    print(starting_value ,end=' ')
    starting_value =starting_value +1
    