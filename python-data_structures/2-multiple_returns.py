def multiple_returns(sentence):
    if not sentence:
        return None
    length = len(sentence)
    first_char = sentence[0]
    print("Length: {:d} - First character: {}".format(length, first_char))
    return length, first_char

multiple_returns("Holberton")