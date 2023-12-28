class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        leset = set(nums)
        longest = 0
        for i in nums:
            if (i-1) not in leset:
                length = 1 
                while (i+length) in leset:
                    length+=1
                longest = max(longest,length)

        return longest


