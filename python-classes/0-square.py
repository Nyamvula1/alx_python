class Square():
    def __init__(self, size=0):
        self.__size = size
        
if __name__ == "__main__":
    square_1 = Square(3)
    print(square_1.__size)
    print(square_1.__dict__)

try:
    print(square_1.__size)
except Exception as e:
    print(e)


    


