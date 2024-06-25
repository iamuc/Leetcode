#https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1={}
        map2={}
        if len(s)!=len(t):
            return False

        for ch in s:
            if ch in map1:
                map1[ch]+=1
            else:
                map1[ch]=1
        for ch in t:
            if ch in map2:
                map2[ch]+=1
            else:
                map2[ch]=1

        for ch in map1:
            if ch not in map2:
                return False
            if map1[ch]!=map2[ch]:
                return False
        return True
