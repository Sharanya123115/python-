#BubbleSort:=push max element to the last (adjacent swapping)
'''def bubbleSort(arr):
    for i in range(n-1,-1,-1):
        for j in range(i):  #starts from 0
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=list(map(int,input().split()))
n=len(arr)
print(bubbleSort(arr))
'''


def bubbleSort(arr):
    arr.sort()
    return arr
arr=list(map(int,input().split()))
print(bubbleSort(arr))