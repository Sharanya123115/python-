#using linear
def nthRoot(n,m):
	ans=-1
	for i in range(n,m+1):
		if(i**n==m):
			ans=i
			break
		elif(i**n>m):
			break
	return ans
n=int(input())
m=int(input())
print(nthRoot(n,m))


#using binary 
'''def nthRoot(n,m):
    low=1
    high=m
    while(low<=high):
        mid=(low+high)//2
        if(mid**n==m):
            return mid
        elif(mid**n>m):
            high=mid-1
        else:
            low=mid+1
    return -1
n=int(input())
m=int(input())
print(nthRoot(n,m))'''