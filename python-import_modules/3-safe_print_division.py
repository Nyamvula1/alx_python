def safe_print_division(a, b):
    if __name__ == '__main__':
        try:
            result = a / b
        except ZeroDivisionError:
            result = None
        finally:
            return "inside result {}".format(result)
        
        
    
    
        