class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #if target - i is in the array return i and j
        hashmap = {}