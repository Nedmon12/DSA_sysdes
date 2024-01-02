class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        holdmin = float("inf")
        while l<r:
            m = (l+r)//2
            holdmin = min(holdmin, nums[m])
            if nums[m] > nums[r]:
                #search right
                l = m + 1
            else:
                r = m -1
        return min(holdmin,nums[l])
