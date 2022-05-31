#!/usr/bin/python3
def print_last_digit(number):
    if(type(number) != int or float):
        return;
    return (number % 10)
