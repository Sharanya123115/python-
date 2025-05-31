def longest(nums,k): #T.C:O(N**2)
    n=len(nums)
    maxLen=0
    for i in range(0,n):
        zero_count=0
        for j in range(i,n):
            if(nums[j]==0):
                zero_count+=1
            if(zero_count>k):
                break
            maxLen=max(maxLen,j-i+1)
    return maxLen
nums=list(map(int,input().split()))
k=int(input())
print(longest(nums,k))