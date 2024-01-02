start with 2 pointers 

calculate the area between them
```
smaller_height * distance_between_pointers
```
compare and store max between current_area and the area we just calculated

move the pointer with the smaller value to the center

```
class Solution:
    def maxArea(self, height: List[int]) -> int:
        lptr, rptr = 0, len(height)
        Bcontainer = 1
        while (lptr < rptr):
            while(lptr < rptr):
                cont = min(height[lptr], height[rptr]) * (rptr-lptr)
                Bcontainer = max(Bcontainer, cont)
                rptr -=1
            lptr +=1
            rptr = len(height)

        return Bcontainer

```