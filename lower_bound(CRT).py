#lowerbound:=smallest element in the array such that arr[ind]>=x   (x=lowerbound)
#array must be in sorted order
def lowerBound(arr,target):
    n=len(arr)
    low=0
    high=n-1
    ans=n
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]>=target):
            ans=mid    #partially stores ans
            high=mid-1
        else:
            low=mid+1
    return ans
arr=list(map(int,input().split()))
target=int(input())
print(lowerBound(arr,target))

#output
'''1 1 1 2 2 2 3 3 4 5 12
2
3   it returns the index value'''