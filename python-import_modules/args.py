import sys
def myarguments(): 
    #talks about how many words were used#(variable name within the sys module calling the particular variable within the module)
    arguments = sys.argv[1:]
    n = len(arguments)
    output = ""
  
    if n == 0:
       output = output  + "0 arguments."
    elif n == 1:
       output += "1 argument: "
    else:
       output += "{} arguments: ".format(n)
       
    #tunatengeza for loop kucheck arguments kwa list(enumerating is numbering and this function will number our argumnets)
    for i, j in enumerate(arguments, 1):
        output += "{}: {}".format(i, j)

    return output.strip()

    
    
       


    
    
    