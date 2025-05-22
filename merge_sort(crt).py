#by using function
'''def ms(nums,n):
    def mergeSort(nums,low,high):  #T.C=O(nlogn)
        if(low>=high):                 #S.C=O(n)
            return
        mid=(low+high)//2
        mergeSort(nums,low,mid)
        mergeSort(nums,mid+1,high)
        sort(nums,low,mid,high)
    def sort(nums,low,mid,high):
        i=low
        j=mid+1
        k=[]
        while(i<=mid and j<=high):
            if(nums[i]<=nums[j]):
                k.append(nums[i])
                i+=1
        while(i<=mid):
            k.append(nums[i])
            i+=1
        while(j<=high):
            k.append(nums[j])
            j+=1
        for ind,val in enumerate(k):
            nums[ind+low]=val        
    low=0
    high=n-1
    mergeSort(nums,low,high)
    return nums
nums=list(map(int,input().split()))
n=len(nums)
print(ms(nums,n))
'''

def ms(nums,n):
    def mergeSort(nums,low,high):
        if(low>=high):
            return
        mid=(low+high)//2 
        mergeSort(nums,low,mid)
        mergeSort(nums,mid+1,high)
        Sort(nums,low,mid,high)
    def Sort(nums,low,mid,high):
        i=low
        j=mid+1
        res=[]
        while(i<=mid and j<=high):
            if(nums[i]<=nums[j]):
                res.append(nums[i])
                i+=1
            else:
                res.append(nums[j])
                j+=1
        while(i<=mid):
            res.append(nums[i])
            i+=1
        while(j<=high):
            res.append(nums[j])
            j+=1
        for ind,val in enumerate(res):
            nums[ind+low]=val 
    low=0
    high=n-1
    mergeSort(nums,low,high)
    return nums
nums=list(map(int,input().split()))
n=len(nums)
print(ms(nums,n))