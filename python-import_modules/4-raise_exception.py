def raise_type_exception():
    try:
        x= raise_type_exception('This is a custom error message')
        return x
    except TypeError as te:
        print("Exception raised")
