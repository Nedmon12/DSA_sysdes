class Solution:
    def minEatingSpeed(self, piles: List[int], h:int )-> int:
        # koko loves to eat bananas
        l, r = 1, max(piles)
        result = max(piles)
        while(l<=r):
            count = 0
            mid = (l+r)//2
            #check whether koko can eat it all 
            for i in piles:
                count = count + math.ceil(i/mid)
            if (count<=h):
                r = mid - 1
                result = min(mid,result)
            else :
                l = mid + 1
        return result


# class Soultion:
    # def minEatingSpeed(self, piles: List[int], h:int )-> int:
    #     # koko loves to eat bananas
    #     l, r = 1, piles[-1]
    #     while(l<=r):
    #         count = 0
    #         mid = (l+r)//2
    #         #check whether koko can eat it all 
    #         for i in piles:
    #             count = count + math.ceil(i/mid)
    #         if (count<h):
    #             r = mid - 1
    #         elif (count>h):
    #             l = mid + 1
    #         else:
    #             return count

