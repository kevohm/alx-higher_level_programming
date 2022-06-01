def finder(str, m):
    ans = ""
    for i in range(0, len(str)):
        if(str[i]!= m):
            ans += str[i]
    return(ans)
