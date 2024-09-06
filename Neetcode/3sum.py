#https://leetcode.com/problems/3sum/
def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums=sorted(nums)
    final=[]
    def twoSum(numbers: List[int], target: int) -> List[int]:
        i,j=0,len(numbers)-1
        output=[]
        while i<j:
            #print(numbers[i],numbers[j],target)
            if numbers[i]+numbers[j]==target:
                output.append([numbers[i],numbers[j],-target])
                i+=1
                j-=1
            elif numbers[i]+numbers[j]>target:
                j-=1
            else:
                i+=1
        return output
    
    for i in range(0,len(nums)-2):
        output=twoSum(numbers=nums[i+1:len(nums)],target=-nums[i])
        for arr in output:
            if arr not in final:
                final.append(arr)
    return final
