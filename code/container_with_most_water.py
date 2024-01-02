class Solution:
    def maxArea(self, height: List[int]) -> int:
        lptr, rptr = 0, len(height) -1
        Bcontainer = 0
        while (lptr < rptr):
            cont = min(height[lptr], height[rptr]) * (rptr-lptr)
            Bcontainer = max(Bcontainer, cont)
            if (height[lptr] < height[rptr]):
                lptr+=1
            else:
                rptr-=1 

        return Bcontainer
