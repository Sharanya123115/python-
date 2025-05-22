#UpperBound:=smallest element in the array such that arr[ind]>x
#array mist be in sorted array
def upperBound(arr,target):
    n=len(arr)
    low=0
    high=n-1
    ans=n
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]>target):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
arr=list(map(int,input().split()))
target=int(input())
print(upperBound(arr,target))

#output
'''1 1 1 2 2 2 3 3 4 5 12
2
6  #it returns index value
'''