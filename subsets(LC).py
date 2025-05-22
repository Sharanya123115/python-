#general method (2 pow no.of elements)EX:-2**3=8
'''def generate(ind,curr,ans,nums):
    if(ind==len(nums)):
        ans.append(curr.copy())
        return
    curr.append(nums[ind])
    generate(ind+1,curr,ans,nums)
    curr.pop()
    generate(ind+1,curr,ans,nums)
def subsets(nums):
    ind=0
    curr=[]
    ans=[]
    generate(ind,curr,ans,nums)
    return ans
nums=list(map(int,input().split()))
print(subsets(nums))'''

#same procedure
def subsets(ind, curr_arr, ans, nums):
    if ind == len(nums):
        ans.append(curr_arr.copy())
        return
    curr_arr.append(nums[ind])
    subsets(ind + 1, curr_arr, ans, nums)
    curr_arr.pop()
    subsets(ind + 1, curr_arr, ans, nums)
    return ans
nums = list(map(int, input().split()))
ind = 0
curr_arr = []
ans = []
print(subsets(ind, curr_arr, ans, nums))

        