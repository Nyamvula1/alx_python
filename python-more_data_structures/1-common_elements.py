def common_elements(set_1, set_2):
    return set_1.intersection(set_2)
    
if __name__ == '__main__':
    set_1 = {"Python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "Perl"}
    
    c_set = common_elements(set_1, set_2)
    
    if c_set:
        for element in sorted(c_set):
            print(element)
    else:
        print("No common elements.")
        
        
        
# for i in set_1, set_2:
     #   return i
#if __name__ == '__main__':
   # set_1 = { "Python", "C", "Javascript" }
    #set_2 = { "Bash", "C", "Ruby", "Perl" }
    #c_set = common_elements(set_1, set_2)
    #print(sorted(list(c_set)))
    