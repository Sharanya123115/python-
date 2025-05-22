#count setbit(ones)
'''a=5
count=0
while a:
    if a&1==1:
        count+=1
    a=a>>1
print(count)'''

#count setbit (zeros)
'''a=int(input())
count=0
while a:
    if a&1!=1:
        count+=1
    a=a>>1
print(count)'''

#count of moves to get 1 after using and operator(1000=8)
'''a=8
count=0
while a&1==0:
    a=a>>1
    count+=1
print(count)'''

#no of moves to get zeros  after and opration
'''a=8
count=0
while a&1!=0:
    a=a>>1
    count+=1
print(count)'''
#another method
'''a=9
count=0
while a&1==1:
    a=a>>1
    count+=1
print(count)'''

#n
"""a=5
count=0
temp=a
while a:
    a=a>>1
    count+=1
while temp&1==0:
    temp=temp>>1
    count-=1
print(count)"""

#convert 1 to 0 as given the index(set 0)
'''def fun(a,i):
    mask=1<<i
    mask=~mask
    return a&mask
a=int(input())
i=int(input())
print(fun(a,i))'''



#set 0
'''def fun(a,i):
    mask=1<<i
    return a | mask
print(fun(8,2))'''

#bit present in the given index 
"""def fun(a,i):
    mask =1<<i
    return 1 if mask&a>0 else 0
print(fun(8,3))"""


#power of 2
'''def fun(a):
    return a&a-1==0
print(fun(8))'''


#even duplicate
'''a=list(map(int,input().split(",")))
res =0
for i in a:
    res ^=i
print(res)'''


#recursion
'''def fun(n):
    if n:
        fun(n-1)
        return n
print(fun(5))'''


'''def fun(n):
    print(n-1)
    fun(n-1)
print(fun(5))'''

#count the number of digits in a number
