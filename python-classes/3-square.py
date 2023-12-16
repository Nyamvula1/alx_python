"""this is a class of my_square.
    It calculates the square size and formats the output
"""
class Square:
    '''initializing size of the square'''
    def __init__(self, size=0):
        self.size = size
    '''initializing the getter'''
    @property
    def size(self):
        return self.__size 
    '''initializing the setter'''
    @size.setter
    def size(self, value):
        if not isinstance(value,int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    
    def area(self):
        return self.__size ** 2
