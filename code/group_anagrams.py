class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        
        for i in range(len(strs)):
            bogusList = []
            sortedList = sorted(strs[i])
            key = ''.join(sortedList)
            if (hashmap.get(key)):
                bogusList = hashmap.get(key)
                bogusList.append(strs[i])
                # hashmap[key] = hashmap[key].extend(strs[i])
                hashmap[key] = bogusList
            else:
                hashmap[key] = [strs[i]]
        returnList = []
        print(hashmap)
        for key in hashmap.values():
            returnList.append(key)
        return returnList