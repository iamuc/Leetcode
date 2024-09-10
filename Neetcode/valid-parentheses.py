#https://leetcode.com/problems/valid-parentheses/
    def isValid(self, s: str) -> bool:
        stack=[]
        parenthesis_map={
            '[':']'
            ,'{':'}'
            ,'(':')'
            }
        for ch in s:
            if ch in parenthesis_map.keys():
                stack.append(ch)
            elif len(stack)==0 or parenthesis_map[stack.pop()]!=ch:
                return False

        return len(stack)==0
