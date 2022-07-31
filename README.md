 <font size="3">

#### List comprehension: 

List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list. 
%: remainder 
```py
list_of_element = [1, 21, 2]
newlist = [x for x in list_of_element if x == 1]
print(newlist)
```
The below example code using the one line if ... else list comprehension converts an odd element to an even by adding 1 to it and adds even elements to the list without performing any operation on them, and as a result, we get a new list of even numbers.

```py
list_of_element = [1, 21, 2]
newlist = [x+1 if x%2 == 1 else x for x in list_of_element]
print(newlist)
```

#### Lambda function: 
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.

###### Syntax: 
```py
lambda arguments : expression
```
###### Example
```py
sum_of_numbers  = lambda a, b : a + b
print(x(5, 6))
```

#### map() function
map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

###### Syntax: 
```PY
map(fun, iter)
```
###### Parameters :
```
fun : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped.
```
###### Returns :
```
Returns a list of the results after applying the given function  
to each item of a given iterable (list, tuple etc.) 
 
 NOTE : The returned value from map() (map object) then can be passed to functions like list() (to create a list), set() (to create a set) .
```
##### Python program to demonstrate working  of map

```py
# Double each List element
def get_double(element: int)->int:
    """
    Double the value of an element 
    param: element 
    return: double of element 
    """
    return element*2

list_of_element = [1, 21, 2]

double_list = map(get_double, list_of_element)
print(list(double_list))
```

We can also use lambda expressions with map to achieve above result.
```py
list_of_element = [1, 21, 2]
double_list = map(lambda i:i*2, list_of_element)
print(list(double_list))
```


##### Download a folder from S3 using Boto3

```py
import os 
import boto3
def download_directory_froms3(bucket_name, remote_directory_path):
    """
    Download a directory from s3 bucket 
    param: s3_bucket_name, remote_directory_path
    """

    s3_resource = boto3.resource('s3',
            aws_access_key_id="<aws_access_key_id>",
            aws_secret_access_key="<aws_secret_access_key>"
            )

    bucket = s3_resource.Bucket(bucket_name) 
    for obj in bucket.objects.filter(Prefix = remote_directory_path):
        if not os.path.exists(os.path.dirname(obj.key)):
            os.makedirs(os.path.dirname(obj.key))
        bucket.download_file(obj.key, obj.key)

download_directory_froms3("bucket_name", "remote_directory_path")
```
##### Convert bytes to specific unit

```py
def convert_bytes(size: int)-> str:
    """
    Convert file size unit 
    param: file_size  
    return: file_size with specific unit 
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0
    return size
```

##### Get file name from the path of file 
```py
def get_file_name(file_path: str)-> str:
    """
    Get the base name in specified path
    param: file_path 
    return: name of the file 
    """
    import os 
    file_name = os.path.basename(file_path)
    return file_name
```

</font>
