'''import class rectangle'''
Rectangle = __import__('7-rectangle').Rectangle
class Square(Rectangle):
    '''initialization of the childclass'''
    def __init__(self, size):
        self.__size= size
        self.integer_validator('size', size)
        '''outputting string format'''
    def __str__(self):
        return '[Square] {}/{}'.format(self.__size,self.__size)
    def area(self):
        return self.__size ** 2
    