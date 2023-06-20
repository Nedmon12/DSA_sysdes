class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #start from an arbitrary position
        #the middle preferably
        # split array into two
        # if greater than left
        # split the right array into 2
        # else split the left half into two
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1