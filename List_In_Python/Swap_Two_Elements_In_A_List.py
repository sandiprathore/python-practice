# Python program to swap two elements in a list
def swap(user_list,pose_1,pose_2):
    user_list = user_list.split(",")
    user_list[pose_1],user_list[pose_2] = user_list[pose_2],user_list[pose_1]
    user_list = [int(i) for i in user_list]
    return user_list

user_list = input("enter elements of list: ")
pose_1 = int(input("element which you want to replace: "))
pose_2 = int(input("Replace With"))
print(swap(user_list,pose_1,pose_2))

