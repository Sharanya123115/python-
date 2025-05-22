#count the no.of digits in a given number using recursion
'''
def fun(n):
    if n//10==0: return 1
    return 1+fun(n//10)
print(fun(0))'''

#sum th given integer
'''def sum(n):
    s=0
    while n>0:
        digit = n%10
        s+=digit
        n=n//10
    return s
n=int(input())
print(sum(n))'''
#another method(using recusion)
'''def fun(n):
    if n//10==0: 
        return n
    return n%10 + fun(n//10)
n=int(input())
print(fun(n)) '''   

# min, max in list
'''def fun(nums):
    def rec(nums,i):
        if i == len(nums)-1:
            return nums[i]
        min = rec(nums,i+1)
        return min if min<nums[i] else nums[i]
    return rec(nums,0)
nums=list(map(int,input().split(",")))
i=int(input())
print(fun(nums))'''


#min,max value
'''def fun(nums):
    def rec(nums,i):
        if i == len(nums)-1:
            return nums[i], nums[i]
        min , max = rec(nums,i+1)
        min = min if min<nums[i] else nums[i]
        max = max if max>nums[i] else nums[i]
        return min,max
    return rec(nums, 0)
nums=list(map(int,input().split(",")))
i=int(input())
min,max=fun(nums)
print(min,max)'''

#find the middle value in the list
def mid(n):
    
n=list(map(int,input().split()))
print(mid(n))







    