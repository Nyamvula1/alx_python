def raise_type_exception():
    try:
        raise Exception("This is a custom error message.")
    except TypeError as te:
        print("Exception raised")
# Example usage:
raise_type_exception()