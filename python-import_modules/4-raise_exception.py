def raise_type_exception():
    try:
        raise TypeError('This is a custom exception')
        
    except TypeError as te:
        print("Exception raised")
        
    
