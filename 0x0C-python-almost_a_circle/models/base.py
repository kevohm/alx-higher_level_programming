# base.py

'''
base of all classes
'''


class Base:
    """base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            seld.id = __nb_objects
