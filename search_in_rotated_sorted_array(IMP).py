#not optimal sol
'''for i in range(nums):  #T.C=O(N)
    if(nums[i]==key):
        return i
return -1'''

#no duplicates
#1.identify the sorted array
#2.check th key is present or not
'''def search(nums,target):     #T.C:=O(logN)
    n=len(nums)
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if(nums[mid]==target):
            return mid
            #left half is sorted
        elif(nums[low]<=nums[mid]):
            if(nums[low]<=target<=nums[mid]):
                high=mid-1
            else:
                low=mid+1
            #right half is sorted
        elif(nums[mid]<=nums[high]):
            if(nums[mid]<=target<=nums[high]):
                low=mid+1
            else:
                high=mid-1
    return -1
nums=list(map(int,input().split()))
target=int(input())
print(search(nums,target))'''

'''#output
7 8 9 1 2 3 4 5 
8
1  #it returns the index value

7 8 9 1 2 3 4 5 
3
5
'''


#contains duplicates elements
def search(arr,key):
    n=len(arr)
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==key):
            return True
        if(arr[low]==arr[mid]==arr[high]):
            low+=1
            high-=1
        elif(arr[low]<=arr[mid]):
            if(arr[low]<=key<=arr[high]):
                high=mid-1
            else:
                low=mid+1
        elif(arr[mid]<=arr[high]):
            if(arr[mid]<=key<=arr[high]):
                low=mid+1
            else:
                high=mid-1
    return False
arr=list(map(int,input().split()))
key=int(input())
print(search(arr,key))

#'''output
# 2 5 6 0  0 1 2
0
True
'''
