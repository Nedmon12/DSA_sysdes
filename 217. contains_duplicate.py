class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numset = set()
        for i in nums:
            if i in numset:
                return True
            numset.add(i)
        return False
    
# Problem number 217
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Solution
# Create hashset
# if number is present in hashset return true
# add number to hashset if not already present in hashset