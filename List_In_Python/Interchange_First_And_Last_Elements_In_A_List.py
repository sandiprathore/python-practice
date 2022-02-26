# Python program to interchange first and last elements in a list
User_list = input("enter elements of list: ")
user_list = User_list.split(",")
user_list[0],user_list[-1] = user_list[-1],user_list[0]
user_list = user_list = [int(i) for i in user_list]
print(user_list)