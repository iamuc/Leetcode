#https://leetcode.com/problems/number-of-1-bits/
class Solution:
    def hammingWeight(self, n: int) -> int:
        #answers lies in way to convert num to bin

        #128 % 2 = 0
        #128 // 2 = 64 % 2 = 0 ....
        #bin = ''
        counter = 0
        while n >= 1:
            if n % 2 == 1:
                counter = counter + 1
            n = n // 2
        return counter
            
            
        
