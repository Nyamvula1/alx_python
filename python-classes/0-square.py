class Square():
    def __init__(self, size=0):
        self.__size = size
        
if __name__ == "__main__":
    my_square = Square(3)
    print(my_square.__size)
    print(my_square.__dict__)

try:
    print(my_square.__size)
except Exception as e:
    print(e)


    


