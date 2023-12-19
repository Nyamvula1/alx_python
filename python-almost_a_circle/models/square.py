'''imports from rectangle class'''
from rectangle import Rectangle
class Square(Rectangle):
    '''initializing the class'''
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        '''calling the class using super'''
        super().__init__(id, x, y, size, size)
    '''method for formatting the string'''
    def __str__(self):
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}'