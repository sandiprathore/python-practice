# python program to find sum of all element present in Array  
print('Enter elements of array: example: 1,2,3.....')
array = input("Enter elements of array: ")
array = array.split(",")
sum = 0
for arr in array:
    arr= float(arr)
    sum = sum + arr
print('Sum of all element peresent in array',sum)