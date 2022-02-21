# Python Program for cube sum of natural numbers in given range
starting_value = int(input("Enter a starting value: "))
ending_value = int(input("Enter the ending value: "))
cube_sum = 0
for digit in range (starting_value, ending_value+1):
    cube_sum = cube_sum + (digit**3)
print(f' The cube sum of digits in range {starting_value} to {ending_value} is {cube_sum}')