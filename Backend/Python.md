Functions can be passed as parameters to other functions because they are objects. Higher-order functions are functions that can take other functions as arguments.  


Python’s argument-passing model is neither “Pass by Value” nor “Pass by Reference” but it is “Pass by Object Reference”.   

Depending on the type of object you pass in the function, the function behaves differently. 
Immutable objects show “pass by value” whereas   
mutable objects show “pass by reference”.    

```py
def call_by_value(x):
    x = x * 2
    print("in function value updated to", x)
    return

def call_by_reference(list):
    list.append("D")
    print("in function list updated to", list)
    return

my_list = ["E"]
num = 6
print("number before=", num)  #6
call_by_value(num)
print("after function num value=", num) #6
print("list before",my_list) # ['E']
call_by_reference(my_list)
print("after function list is ",my_list) #['E', 'D']

```

lambda function is an anonymous function. This function can have any number of parameters but, can have just one statement.  

```py
s2 = lambda func: func.upper()
print(s2(s1))
```

*args is used to pass a variable number of arguments to a function. 
for example multiple strings, numers, variables 

```py
def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
```

**kwargs allows the function to accept any number of arguments with key-value pairs.  
```py
def fun(**kwargs):
    for k, val in kwargs.items():
        print("%s == %s" % (k, val))


# Driver code
fun(s1='Geeks', s2='for', s3='Geeks') 
```

a = [10, 20, 40, True] 
tup1 = (0, 1, 2, 3) //immutable
my_set = {1, 2, 3}
my_dict = {“a”: 1, “b”: 2, “c”: 3}


Exceptional handling -try, except and finally  
```py
n = 10
try:
    res = n / 0  # This will raise a ZeroDivisionError
    
except ZeroDivisionError:
    print("Can't be divided by zero!")
```

Array - homogenous data , list - heterogenous data 

A module is a single file that contains Python code (functions, variables, classes) which can be reused in other programs. You can think of it as a code library. For example: math is a built-in module that provides math functions like sqrt(), pi, etc.  

package is a collection of related modules stored in a directory. It helps in organizing and grouping modules together for easier management. For example: The numpy package contains multiple modules for numerical operations.   

To create a package, the directory must contain a special file named __init__.py.  

