def sumK(arr,k):
    n=len(arr)
    d={}
    Sum=0
    maxLen=0
    for i in range(0,n):
        Sum+=arr[i]
        if(Sum==k):
            maxLen=i+1
        rem=Sum-k
        if(rem in d):
            maxLen=max(maxLen,i-d[rem])
        if(Sum not in d):
            d[sum]=i
    return maxLen
arr=list(map(int,input().split()))
k=int(input())
print(sumK(arr,k))
    