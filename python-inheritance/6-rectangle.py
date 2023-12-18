'''imports class basegeometry'''
BaseGeometry = __import__('5-base_geometry').BaseGeometry
'''inherits from class basegeometry'''
class Rectangle(BaseGeometry):
    '''initialization of the childclass'''
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator('width', width)
        self.integer_validator('width', height)