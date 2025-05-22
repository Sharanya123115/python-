#gfg
def findKrotation(arr):
    n=len(arr)
    low=0
    high=n-1
    Min=float("inf")
    mIndex=-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[low]<=arr[mid]):
            if(arr[low]<Min):
                Min=arr[low]
                mIndex=low
            low=mid+1
        if(arr[mid]<=arr[high]):
            if(arr[mid]<Min):
                Min=arr[mid]
                mIndex=mid
            high=mid-1
    return mIndex
arr=list(map(int,input().split()))
print(findKrotation(arr))

#output
'''5 1 2 3 4
1

7 8 9 2 3 4
3
'''