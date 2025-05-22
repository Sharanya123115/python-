#using linear
'''from math import *
def kokoEat(arr,k):
    for noOfBanana in range(1,max(arr)+1):
        time=0
        for num in arr:
            time+=ceil(num/noOfBanana)
        if(time<=k):
            return noOfBanana
arr=list(map(int,input().split()))
k=int(input())
print(kokoEat(arr,k))
'''

#using binary
from math import *
def kokoEat(arr,k):
    low=1
    high=max(arr)
    while(low<=high):
        noOfbanana=(low+high)//2
        time=0
        for num in arr:
            time+=ceil(num/noOfbanana)
        if(time<=k):
            high=noOfbanana-1
        else:
            low=noOfbanana+1
    return low
arr=list(map(int,input().split()))
k=int(input())
print(kokoEat(arr,k))
