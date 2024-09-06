#https://leetcode.com/problems/container-with-most-water
def maxArea(self, height: List[int]) -> int:
    #O(n)
    i,j=0,len(height)-1
    output=0
    #Target= MAX((j-i)*MIN(height[i],height[j]))
    while i<j:
        water=(j-i)*min(height[i],height[j])
        #print(i,j,water)
        if water>output:
            output=water
        
        if height[i]<height[j]:
            i+=1
        else:
            j-=1
    return output
