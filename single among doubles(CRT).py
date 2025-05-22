#1 1 2 2 3 3 4 5 5 6 6
#0 1 2 3 4 5 6 7 8 9 10
#normal method with T.C O(2N)
'''d={} #using dictionary
for i in arr:
    if(i in d):
        d[i]=d[i]+1
    else:
        d[i]=1
    for key,value in d.items:
        if(value==1):
            return key
'''

#gfg,LL(single element in a sorted array),code360
#(even,odd)-->left half&single is at right side
#(odd,even)--->right half $ single is at left side
def findOnce(nums):   #T.c=O(logN)
    n=len(nums)
    if(n==1):
        return nums[0]
    elif(nums[0]!=nums[1]):
        return nums[0]
    elif(nums[n-1]!=nums[n-2]):
        return nums[n-1]
    low=1
    high=n-2
    while(low<=high):
        mid=(low+high)//2
        if(nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]):
            return nums[mid]
        #you are on the left half so single ele in right side
        elif((mid%2==1 and nums[mid]==nums[mid-1]) or (mid%2==0 and nums[mid]==nums[mid+1])):
            low=mid+1
        #you are on right half so single ele on left side
        elif((mid%2==0 and nums[mid]==nums[mid-1]) or (mid%2==1 and nums[mid]==nums[mid+1])):
            high=mid-1
nums=list(map(int,input().split()))
print(findOnce(nums))

