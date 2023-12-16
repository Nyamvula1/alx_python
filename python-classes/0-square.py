'''This a square class that is used to return the size of the square'''
class Square():
    '''I am now initializing the size of the class'''
    def __init__(self, size):
        self.__size = size
        
'''This indicates that mysquare is an instance of the Square class, and the dictionary containing the size is printed as expected.'''       
if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)
    
   

   

   


    


