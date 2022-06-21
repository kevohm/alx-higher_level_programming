#!/usr/bin/python3
#!/usr/bin/python3


# 5-square.py


""" class of square """


class Square:

    """ inside square """
    def __init__(self, size=0):
        """
        Args:
            size (int): integer
        """
        if size != int(size):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """ Get and set """
        return self.__size

    @size.setter
    def size(self, value):
        if value != int(value):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ area of square """
        return pow(self.__size, 2)

    def my_print(self):
        """ print to stdout """
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
