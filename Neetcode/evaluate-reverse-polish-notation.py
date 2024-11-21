#https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def operate (num1:int, num2:int, operand:str) -> int:
            match operand:
                case '+':
                    return num1+num2
                case '-':
                    return num1-num2
                case '/':
                    return int(num1/num2)
                case '*':
                    return num1*num2

        operators=['+','-','/','*']
        stack=[]
        for token in tokens:
            #print(stack)
            if token in operators:
                num1=int(stack.pop())
                num2=int(stack.pop())
                result=operate(num2,num1,token)
                stack.append(result)
            else:
                stack.append(token)
        
        return int(stack[0])
