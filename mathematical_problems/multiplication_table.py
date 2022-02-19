#take input from the user 
number=int(input("Enter the number: "))
#print the table using for loop 
for multiplayer in range (1,11):
    table = number * multiplayer
    print(f'{number} * {multiplayer} = {table}' )
