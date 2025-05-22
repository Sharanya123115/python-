if(n<0):
    x=1/x
n=abs(n)
ans=1
for i in range(n):
    ans=ans*x
return ans