monotonic decreasing stack problem

while iterating through the list
append index and value on a stack
if current item greater than top of stack 

pop every item from the stack that is less than current item

and update stack accordingly

```
current index - index from stack goes to array[current index]
```
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

```
