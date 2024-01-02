class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newarray = []
        newarray = [0 for i in range(2*len(nums))]
        n = len(nums)
        for i in range(len(nums)):
            newarray[i] = nums[i]
            newarray[i+n] = nums[i]

        return newarray