def common_elements(set_1, set_2):
    set_1 = { "Python", "C", "Javascript" }
    set_2 = { "Bash", "C", "Ruby", "Perl" }
    
    return set_1, set_2
if __name__ == '__main__':
    set_1, set_2  = common_elements(set(), set())
    c_set = set_1.intersection(set_2)
    print(sorted(list(c_set)))
    