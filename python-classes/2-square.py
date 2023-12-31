'''This a square class that is used to return the size of the square'''
class Square():
    '''I am now initializing the size of the class'''
    def __init__(self, size=0):
        '''isinstance is used to check the type of data in a parameter'''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError ('size must be >= 0')
        else:
            self.__size = size
        
    def area(self):
        return self.__size ** 2
if __name__ == '__main__':
    my_square_1 = Square(3)
    print("Area: {}".format(my_square_1.area()))

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    my_square_2 = Square(5)
    print("Area: {}".format(my_square_2.area()))