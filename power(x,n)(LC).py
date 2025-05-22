'''def myPow(x,n):
    if n<0:
        x=1/x
    n=abs(n)
    ans=1
    for i in range(n):
        ans=ans*x
    return ans
n=int(input())
x=int(input())
print(myPow(x,n))'''


#using recursion(optimal solution)
'''def pow(x,n):
    if(n==0):
        return 1
    if(n%2==1):
        return x*pow(x,n-1)
    return pow(x*x,n//2)
    if (n<0):
       x=1/x
    n=abs(n)
n=int(input())
x=int(input())
print(pow(x,n))
'''

#no idea on code
def power(n):
    for i in range(31):
        if(2**i==n):
            return True
    return False
n=int(input())
print(power(n))