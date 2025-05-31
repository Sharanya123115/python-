'''def maxSubarray(nums):
    n=len(nums)
    maxSum=float("-inf")
    for i in range(0,n):
        for j in range(i,n):
            Sum=sum(nums[i:j+1])
            maxSum=max(maxSum,Sum)
    return maxSum
nums=list(map(int,input().split()))
print(maxSubarray(nums))
#nums:-2 -1 3 4 6 -1 -6 10 20
#output:36
'''
#optimal solution
def maxSubarray(num):
    n=len(nums)
    maxSum=float("-inf")
    currentSum=0
    for i in nums:
        currentSum+=i
        maxSum=max(maxSum,currentSum)
        if(currentSum<0):
            currentSum=0
    return maxSum
nums=list(map(int,input().split()))
print(maxSubarray(nums))
#nums=-2 -1 3 4 6 -1 -6 10 20
#output=36
