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
        return self.__height
    
    '''sets and returns the value of the parameter assigned to the width'''
    @width.setter
    def width(self, value):
        self.__width= value
    
    @property
    def height(self):
        return self.__height
      
    @height.setter
    def height(self, value):
        self.__height= value
        
    @property
    def x(self):
        return self.__x
      
    @x.setter
    def x(self, value):
        self.__x= value
        
    @property
    def y(self):
        return self.__y
      
    @y.setter
    def y(self, value):
        self.__y= value
    