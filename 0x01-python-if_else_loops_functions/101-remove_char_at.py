#!/usr/bin/python3
def remove_char_at(str, m):
    ans = ""
    for i in range(0, len(str)):
        if(i != m):
            ans += str[i]
    return(ans)
