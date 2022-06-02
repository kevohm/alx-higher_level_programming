#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    for i in range(0, length):
        printf("{}: {}". format(i, sys.argv[i]))
