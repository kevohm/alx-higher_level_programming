#!/usr/bin/python3

def print_last_digit(number):
    if(type(number) != int or float):
        print("Traceback (most recent call last):")
        pass
    a = abs(number) % 10
    return (a)
