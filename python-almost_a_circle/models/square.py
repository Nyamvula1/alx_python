'''imports from rectangle class'''
from models.rectangle import Rectangle
class Square(Rectangle):
    '''initializing the class'''
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        '''calling the class using super'''
        super().__init__(size, size, x, y, id)
    '''method for formatting the string'''
    def __str__(self):
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}'
    '''function for getting and setting the attributes and returns the width and height'''
    @property
    def size(self):
        return self.__width
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('Width must be > 0')
    
        self.__width = value
        self.__height = value
    
   

# if __name__ == "__main__":

#     s1 = Square(5)
#     print(s1)
#     print(s1.size)
#     s1.size = 10
#     print(s1)

#     try:
#         s1.size = "9"
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))