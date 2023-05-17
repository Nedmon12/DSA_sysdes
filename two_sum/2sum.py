class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #if target - i is in the array return i and j
        for i in range(len(nums)):
            #search in array
            for j in range(len(nums)):
                if ((nums[i]+nums[j])==target and i!=j):
                    return [i,j]
                j = j+1
            i = i+1
        