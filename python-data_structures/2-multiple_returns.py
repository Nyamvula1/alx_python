def multiple_returns(sentence):
    
    if len(sentence) < 0:
        return None

    length = len(sentence)
    first_char = sentence[0]
    return length, first_char

if __name__ == '__main__':
    sentence = "At Holberton school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))
    
    
    