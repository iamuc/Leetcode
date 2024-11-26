#https://leetcode.com/problems/generate-parentheses/
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]

        def backtrack(openN, closedN):
            #Exit condition
            if openN==closedN==n:
                res.append(''.join(stack))
                return
            #Constraint1
            if openN < n:
                stack.append("(")
                #print("added ( to stack")
                backtrack(openN+1,closedN)
                #print(f"backtrack with {openN}+1,{closedN}")
                stack.pop()
            #Constraint2
            if closedN < openN:
                stack.append(")")
                #print("added ) to stack")
                backtrack(openN,closedN+1)
                #print(f"backtrack with {openN},{closedN}+1")
                stack.pop()
        backtrack(0,0)
        return res
