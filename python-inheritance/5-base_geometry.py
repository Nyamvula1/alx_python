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