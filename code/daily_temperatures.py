class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        returnList = [0] * len(temperatures)

        for i, c in enumerate(temperatures):
            while stack and c > stack[-1][0]:
                stackValue, stackIndex = stack.pop()
                returnList[stackIndex] = i - stackIndex
            stack.append((c,i))

        return returnList

            

