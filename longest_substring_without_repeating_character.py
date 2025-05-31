def Substring(s):#T.C:O(N**2) , S.C:O(256)
    n=len(s)
    maxLen=0
    for i in range(0,n):
        checker=[0]*256
        for j in range(i,n):
            if(checker[ord(s[j])]==1):
                break
            checker[ord(s[j])]=1
            maxLen=max(maxLen,j-i+1)
    return maxLen
s=input()
print(Substring(s))