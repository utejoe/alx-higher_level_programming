#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_char = None if not sentence else sentence[0]
    sentence_tuple = (length, first_char)
    return sentence_tuple
