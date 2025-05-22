#Insertion sort:=takes an element and place in correct place
'''def insertionSort(arr):
    n=len(arr)
    for i in range(0,n):
        while(i>0 and arr[i-1]>arr[i]):
            arr[i-1],arr[i]=arr[i],arr[i-1]
            i-=1
    return arr
arr=list(map(int,input().split()))
print(insertionSort(arr))'''


#accenture question
s="hey hii hello"
s=s.split(" ")
s=s[::-1]
#print(*s)  
print(" ".join(s))