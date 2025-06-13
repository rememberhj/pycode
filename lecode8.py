
def finlsrt(strs):
    strs.sort(key=len)
    if(len(strs)==1):
        return strs
    endstr=""
    for k in range(len(strs[0])):
        for j in range(1,len(strs)):
         if(strs[0][k]==strs[j][k]):
            if(j==len(strs)-1):
                endstr+=strs[0][k]
         elif (strs[0][k]!=strs[j][k]):
                return endstr

    return endstr
print(finlsrt(["flower","flow","flight"]))


    