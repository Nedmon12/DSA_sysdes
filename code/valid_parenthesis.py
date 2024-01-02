class Solution:
    def isValid(self, s: str) -> bool:
        #scan items from the array
        #push opening braces on the stack
        #pop an item from the stack if{conditiontoolong}
        #return error if {conditionlongagain}
        stack = []
        mappings = {")": "(", "}": "{", "]": "["}
        for i in range(len(s)):
            if not s[i] in mappings:
                stack.append(s[i])
                continue
                # print(top_element)
            if not stack or stack[-1] != mappings[s[i]]:
                return False
            stack.pop()
        return not stack