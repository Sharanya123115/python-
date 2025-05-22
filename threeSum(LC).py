#3sum using three pointers(first method) time limit exceeds
'''def threeSum(nums,target):  #T.C:-O(N**3)
    triplet_sum=set()
    n=len(nums)
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if(nums[i]+nums[j]+nums[k]==0):
                    temp=[nums[i],nums[j],nums[k]]
                    temp.sort()
                    triplet_sum.add(tuple(temp))
    ans=[]
    for triplet in triplet_sum:
        ans.append(list(triplet))
    return ans
nums=list(map(int,input().split()))
target=int(input())
print(threeSum(nums,target))
'''
#using array(2pointers)
'''def threeSum(nums,target):  #T.c=O(N**2)
    triplet_sum=set()
    n=len(nums)
    for i in range(0,n-1):
        hashmap=[]
        for j in range(i+1,n):
            k=-(nums[i]+nums[j])
            if(k in hashmap):
                temp=[nums[i],nums[j],k]
                temp.sort()
                triplet_sum.add(tuple(temp))
            hashmap.append(nums[j])
    ans=[]
    for triplet in triplet_sum:
        ans.append(list(triplet))
    return ans
nums=list(map(int,input().split()))
target=int(input())
print(threeSum(nums,target))

'''

#optimal solution
def threeSum(nums,target): 
    nums.sort()
    n=len(nums)
    ans=[]
    for i in range(0,n):
        if(i>0 and nums[i]==nums[i-1]):
            continue
        j=i+1
        k=n-1
        while(j<k):
            Sum=nums[i]+nums[j]+nums[k]
            if(Sum<0):
                j+=1
            elif(Sum>0):
                k-=1
            else:
                temp=[nums[i],nums[j],nums[k]]
                ans.append(temp)
                j+=1
                k-=1
                while(j<k and nums[j-1]==nums[j]):
                    j+=1
                while(j<k and nums[k+1]==nums[k]):
                    k-=1
    return ans
nums=list(map(int,input().split()))
target=int(input())
print(threeSum(nums,target))

            