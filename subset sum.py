def check(self,ind,arr,sum):
    if(sum==0):
        return True
    if(sum<0):
        return False
    if(ind==len(arr)):
        return False
    path1=slef.check(ind+1,arr,sum-arr[ind])
    if(path1==True):
        return True
    path2=self.check(ind+1,arr,sum)
    return path1 or path2
def issubsetSum(self, arr, sum):
    ind=0
    return self.check(ind,arr,sum)


    