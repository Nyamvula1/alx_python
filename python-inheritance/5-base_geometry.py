'''initializing the class'''
class BaseGeometry:
    '''method 1'''
    def area(self):
        '''raises the exception message'''
        raise Exception('area() is not implemented')
    '''returns if value is an integer, 
    isinstance is used to checkif the value passed is an inetger'''
    def integer_validator(self, name, value): 
        if not isinstance(value,int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
        def __dir__(self):
            return sorted(['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'integer_validator'])