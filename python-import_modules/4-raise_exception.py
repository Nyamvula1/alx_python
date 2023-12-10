def raise_type_exception():
    try:
        raise TypeError("This is a custom type exception.")
    except TypeError as e:
        print(f"Caught an exception: {e}")

# Example usage:
raise_type_exception()