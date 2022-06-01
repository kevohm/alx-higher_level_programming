#!/usr/bin/python3
def finder(str, m):
    ans = ""
    for i in range(0, len(str)):
        if(i != m):
            ans += str[i]
    return(ans)
