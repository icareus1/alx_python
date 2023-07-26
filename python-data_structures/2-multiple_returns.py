def multiple_returns(sentence):
    if len(sentence) == 0:
        return None
    first_char = sentence[0]
    length = len(sentence)
    return (length,first_char)