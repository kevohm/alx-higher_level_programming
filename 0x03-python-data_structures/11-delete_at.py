#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    cpy = []
    if (len(my_list) != 0) and (idx > 0) and (idx < len(my_list)):
        for i in range(len(my_list)):
            if i == idx:
                continue
            cpy.append(my_list[i])
    else:
        return my_list
    return cpy
