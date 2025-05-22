#gfg
#using linear approach(Time limit Exceeds)
'''from math import *
def smallestDivisor(arr,k):
    for div in range(1,max(arr)+1):
        sum=0
        for num in arr:
            sum+=ceil(num/div)
        if(sum<=k):
            return div
arr=list(map(int,input().split()))
k=int(input())
print(smallestDivisor(arr,k))
'''

#binary 
from math import *
def smallestDivision(arr,k):
    low=1
    high=max(arr)
    while(low<=high):
        div=(low+high)//2
        sum=0
        for num in arr:
            sum+=ceil(num/div)
        if(sum<=k):
            high=div-1
        else:
            low=div+1
    return low
arr=list(map(int,input().split()))
k=int(input())
print(smallestDivision(arr,k))