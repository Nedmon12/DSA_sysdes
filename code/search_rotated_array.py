class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l<r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            # [0,1,2,4,5,6,7]
            # [4,5,6,7,0,1,2]
            # [5,6,7,0,1,2,4]
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1

            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
