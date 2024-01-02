class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        sCount, tCount = {}, {}

        for c in s:
            sCount[c] = sCount.get(c,0) + 1
            print(sCount[c])
        for f in t:
            tCount[f] = sCount.get(f,0) + 1
        for x in s:
            if (tCount[x] != sCount[x]):
                return False
    isAnagram("anagram","angrama")