#!/usr/bin/python3
def print_last_digit(number):
    if(type(number) != int or float):
        return;
    a = abs(number) % 10
    return (a)
