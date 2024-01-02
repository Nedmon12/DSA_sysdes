class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            #if token = int
            # stack. append
            #else 
            # new item = stack[-2] operand [stack-1]
            # pop them and append(new item)
            # if (token.isalnum()):
            #     stack.append(int(token))
            if(token=="+"):
                newItem = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(newItem)
            elif(token=="-"):
                newItem = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(newItem)
            elif(token=="/"):
                newItem = stack[-2] / stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(newItem))
            elif(token=="*"):
                newItem = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(newItem)
            else:
                stack.append(int(token))
        return stack[-1]



    #     class Solution:
    # def evalRPN(self, tokens: List[str]) -> int:
    #     stack = []
    #     if(len(tokens)==1):
    #         return tokens[0]
    #     for token in tokens:
    #         #if token = int
    #         # stack. append
    #         #else 
    #         # new item = stack[-2] operand [stack-1]
    #         # pop them and append(new item)
    #         if(stack[-2]):
    #             bottom = stack[-2]
    #         if (token.isalnum()):
    #             stack.append(int(token))
    #         else:
    #             if(token=="+"):
    #                 newItem = stack[-2] + stack[-1]
    #                 stack.pop()
    #                 stack.pop()
    #                 stack.append(newItem)
    #             if(token=="-"):
    #                 newItem = stack[-2] - stack[-1]
    #                 stack.pop()
    #                 stack.pop()
    #                 stack.append(newItem)
    #             if(token=="/"):
    #                 newItem = stack[-2] / stack[-1]
    #                 stack.pop()
    #                 stack.pop()
    #                 stack.append(newItem)
    #             if(token=="*"):
    #                 newItem = stack[-2] * stack[-1]
    #                 stack.pop()
    #                 stack.pop()
    #                 stack.append(newItem)
    #     return stack[-1]