'''
This function is_same_class takes two arguments, obj and a_class, 
and it returns True if the class of obj is the same as the specified a_class, 
and False otherwise.
'''
def is_same_class(obj, a_class):
    return obj.__class__ is a_class
'''
You initialize a variable a with the value 1.
'''
a = 1
'''
Here, you use the is_same_class function to check whether 
a is an instance of the classes int, float, and object.
If a is an instance of a class, it prints a corresponding message.
'''
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
elif is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
elif is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))
'''
You call the is_same_class function for each of the classes (int, float, and object) 
and store the results in result_int, result_float, and result_object. 
Then, you print these results.
'''
#result_int = is_same_class(a, int)
#result_float = is_same_class(a, float)
#result_object = is_same_class(a, object)

#print(result_int)     # Output: True
#print(result_float)   # Output: False
#print(result_object)


