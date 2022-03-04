# dictionary
dic = {"coconut": 5, "banana": 2, "apple": 3}

# method: 1 
# get Size of dictinory in bytes by "sys" module
import sys
size_of_dictionary_m1 = str(sys.getsizeof(dic) )+ " bytes"
print(f"The size of dictionary is {size_of_dictionary_m1}")


# method: 2
# get Size of dictinory in bytes by __sizeof__() method
# no need to import any module for this method
size_of_dictionary_m2 = str(dic.__sizeof__()) + ' bytes'
print(f"The size of dictionary is {size_of_dictionary_m2}")

