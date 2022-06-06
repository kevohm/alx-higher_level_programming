#!/usr/bin/python3
def no_c(my_string = "mychat"):
    s = ""
    for i in my_string:
        if i == "c":
            s += "C"
        s += i
    return s
