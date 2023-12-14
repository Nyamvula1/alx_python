class Square():
    def __init__(self, size=0):
        self.__size = size
        self.dict__ = {size : self.__size}
 #This indicates that mysquare is an instance of the Square class, and the dictionary containing the size is printed as expected.       
if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square.__size))
    print(my_square.dict__)

try:
    print(my_square.__size)
except Exception as e:
    print(e)


    


