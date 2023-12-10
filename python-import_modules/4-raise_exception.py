def raise_type_exception():
    try:
        raise TypeError('This is a custom exception')
        
    except TypeError:
        print("Exception raised")
        
    
if __name__ == '__main__': 
    x = raise_type_exception
    print(x)
raise_type_exception()
