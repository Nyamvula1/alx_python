'''imports from base class'''
from models.base import Base
'''initializing the class'''
class Rectangle(Base):
    '''creating instances of the class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height =height
        self.x = x
        self.y = y
        '''calls the function from the base class'''
        super().__init__(id)
        '''uses @property to get and returns as a private variable'''
    @property
    def width(self):
        return self.__width
    
    '''sets and returns the value of the parameter assigned to the width'''
    @width.setter
    def width(self, value):
        
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width= value
        
    @property
    def height(self):
        return self.__height
    '''sets and returns the value of the parameter assigned to the height'''  
    @height.setter
    def height(self, value):
        '''checks if the value is an integer or if value is less than zero, it returns the variable as the value'''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height= value
        
    @property
    def x(self):
        return self.__x
      
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x= value
        
    @property
    def y(self):
        return self.__y
      
    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y= value
    '''method for returning the area of the rectangle'''
    def area(self):
        return self.__width * self.__height
    '''this is done by using the instances and multiplying'''