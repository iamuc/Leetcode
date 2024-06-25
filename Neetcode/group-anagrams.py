#https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map={}
        strsSorted=[]
        for str in strs:
            #Create a count map
            map[str]={}
            for char in str:
                if char in map[str]:
                    map[str][char]+=1
                else:
                    map[str][char]=1

            #Use this map to genrate a string in sorted order
            str0=''
            for ch in sorted(map[str].keys()):
                str0 += ch*map[str][ch]
            strsSorted.append(str0)

        #Use this sorted list to get anagrams
        anagrams={}
        for i in range(0,len(strsSorted)):
            if strsSorted[i] in anagrams:
                anagrams[strsSorted[i]].append(i)
            else:
                anagrams[strsSorted[i]]=[i]

        #Retrive the results
        result=[]
        for idk, key in enumerate(anagrams.keys()):
            result.append([])
            for val in anagrams[key]:
                result[idk].append(strs[val])

        return result

#Next Steps: Can we somehow weight the chars by frequncy to get a unique value which we can use to compare
