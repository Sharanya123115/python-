def check(self,ind,arr,target):
    if(target==0 and ind=len(arr)):
        return 1
    if(target<0):
        return 0
    if(ind==len(arr)):
        return 0
    path1=self.check(ind+1,arr,target-arr[ind])
    path2=self.check(ind+1,arr,target)
    return path1+path2
def perfectSum(self,arr,target):
    ind=0
    return self.check(ind,arr,target)]  