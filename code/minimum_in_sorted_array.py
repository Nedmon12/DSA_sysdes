class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        # min = nums[0]
        holdmin = float("inf")
        while l<r:
            m = (l+r)//2
            holdmin = min(holdmin, nums[m])
            if nums[m] > nums[r]:
                #search right
                l = m + 1
            else:
                #search left
                r = m -1
        return min(holdmin,nums[l])
