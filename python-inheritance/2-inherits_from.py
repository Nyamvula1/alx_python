'''
This function is_same_class takes two arguments, obj and a_class, 
and it returns True if the class of obj is the same as the specified a_class, 
and False otherwise.
'''
def inherits_from(obj, a_class):
    '''returns false if object is not a derived class from a_class'''
    if type (obj) is a_class:
        return False
    '''checks the object is a derived class from a_class'''
    return issubclass (type (obj), a_class)
