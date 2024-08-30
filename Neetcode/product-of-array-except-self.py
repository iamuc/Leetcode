#https://leetcode.com/problems/product-of-array-except-self/

def productExceptSelf(self, nums: List[int]) -> List[int]:
    output=[1]*len(nums)
    
    prefix=1
    suffix=1

    for i in range(0,len(nums)):
        output[i] *= prefix
        prefix*=nums[i]

    for i in range(len(nums)-1,-1,-1):
        output[i] *= suffix
        suffix*=nums[i]

    return output
