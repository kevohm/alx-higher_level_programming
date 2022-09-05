#!/usr/bin/python3
# 5-text_indentation
'''5-text_indentation module

prints a text with 2 new lines after each of these characters: ., ? and :

'''


def text_indentation(text):
    '''function text_indentation
    prints a text
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    arr = ['.', '?', ':']
    for i in range(len(text)):
        print(text[i], end="")
        for j in arr:
            if j == text[i]:
                print("")
                print("")
