def raise_type_exception():
    try:
        raise_type_exception('')
        
    except TypeError as te:
        print("Exception raised")
        return te
        
    
