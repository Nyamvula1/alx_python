def safe_print_division(a, b):
    try:
        result = a / b
        error = e
        return result
    except error as e:
        print ("division error has occured")   
    else:
        print("{} / {} = {}".format(a, b, result))
        return None
        

    finally:
        print("inside result {}".format(result))
        return result
        
    
    
        