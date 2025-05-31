def Substring(s):
    n=len(s)
    maxLen=0
    left=0
    right=0
    d={}
    while(right<n):
        if(s[right] in d):
            if(d[s[right]]>=left):
                left=d[s[right]]+1
        d[s[right]]=right
        maxLen=max(maxLen,right-left+1)
        right+=1
    return maxLen
s=input()
print(Substring(s))
#s:abcabcccb
#output:3'''