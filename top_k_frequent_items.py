class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1
        sorted_x = sorted(hashmap.items(), key=operator.itemgetter(1))
        # sorted_dict = collections.OrderedDict(sorted_x)
        print(sorted_x[-1][0])
        returnList = []
        for i in range(k):
            returnList.append(sorted_x[-(i+1)][0])
        return returnList