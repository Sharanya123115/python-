def quick(arr,low,high):
    if(low<high):
        pIndex=partition(arr,low,high)
        quick(arr,low,pIndex-1)
        quick(arr,pIndex+1,high)
def partition(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while(i<j):
        while(arr[i]<=pivot and i<=high-1):
            i+=1
        while(arr[j]>pivot and j>=low+1):
            j-=1
        if(i<j):
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j
arr=list(map(int,input().split()))
quick(arr,0,len(arr)-1)
print(arr)