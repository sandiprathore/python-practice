input_string = input("Enter your string ")
input_string=input_string.lower().strip()
vol=0
con = 0
for i in range (0,len(input_string)):
    if input_string[i] == "a" or input_string[i] =="e" or input_string[i] =="i"  or input_string[i] =="o" or input_string[i] == "u" or input_string[i] == "y":
        vol = vol + 1
    else:
        con = con + 1 
print(f'{vol} vowels and {con} consonant  in "{input_string}"')