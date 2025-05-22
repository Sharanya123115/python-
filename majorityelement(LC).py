#majority element1
'''def majorityElements(nums):
    d={}
    n=len(nums)
    for i in nums:
        if(i in d):
            d[i]=d[i]+1
        else:
            d[i]=1
    for key,value in d.items():
        if(value>n//2):
            return key
nums=list(map(int,input().split()))
print(majorityElements(nums))'''

#majority element 2
def majorityElements(nums):
    d={}
    n=len(nums)
    for i in nums:
        if(i in d):
            d[i]=d[i]+1
        else:
            d[i]=1
    ans=[]
    for key,value in d.items():
        if(value>n//3):
            ans.append(key)
    return ans
nums=list(map(int,input().split()))
print(majorityElements(nums))
