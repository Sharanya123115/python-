def fruits_into_baskets(fruits):#T.C:O(N**2)
    n=len(fruits)
    maxLen=0
    for i in range(0,n):
        s=set()
        for j in range(i,n):
            s.add(fruits[j])
            if(len(s)>2):
                break
            maxLen=max(maxLen,j-i+1)
    return maxLen
fruits=list(map(int,input().split()))
print(fruits_into_baskets(fruits))