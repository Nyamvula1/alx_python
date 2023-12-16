"""This a square class that is used to return the size of the square
    and the area of a square using the value of the square.
"""
class Square():
    
    '''I am now initializing the size of the class'''   
    def __init__(self, size=0):
        '''isinstance is used to check the type of data in a parameter'''
        self.size = size
        
    '''this is a method used to privatize the size'''
    '''gets the size and returns as private'''
    @property
    def size(self): 
        return self.__size 
    
    '''sets the value of the size '''
    @size.setter
    def size (self, value):
        '''isinstance is used to check the type of data in a parameter'''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError ('size must be >= 0')
        else:
            self.__size = value
              
    def area(self):
        return self.__size ** 2
if __name__ == '__main__':
    my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)
