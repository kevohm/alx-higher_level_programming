#!/usr/bin/python3

def fizzbuzz():
    for i in range(1, 101):
        w = i % 3
        s = i % 5
        if(w == 0 and s == 0):
            print("FizzBuzz",end=" ")
        elif(s == 0):
            print("Buzz",end=" ")
        elif(w == 0):
            print("Fizz",end=" ")
        else:
            print("{}".format(i),end=" ")
