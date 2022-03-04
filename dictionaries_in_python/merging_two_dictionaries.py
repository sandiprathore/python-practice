
first_dict = {"name":"raja", "age":42,"city":"indore"}
second_dict = {"address":"rajwada", "subject":"B.tech"}

# using .update() method 
first_dict.update(second_dict)
print(first_dict)



# Using ** method 
updated_dict = {**first_dict, **second_dict}
print(updated_dict)