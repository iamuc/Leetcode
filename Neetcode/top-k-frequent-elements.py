#https://leetcode.com/problems/top-k-frequent-elements/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map={}
        for num in nums:
            if num in map:
                map[num]+=1
            else:
                map[num]=1
        #We have frequncy of each num now
        freqs={}
        for num in map:
            freq=map[num]
            if freq in freqs:
                freqs[freq].append(num)
            else:
                freqs[freq]=[num]

        nums0=[]
        n=1
        for freq in sorted(freqs.keys(),reverse=True):
            print(freq)
            for i in freqs[freq]:
                if n<=k:
                    nums0.append(i)
                    n+=1
                else:
                    break
            if n>k:
                break
                
        return nums0
