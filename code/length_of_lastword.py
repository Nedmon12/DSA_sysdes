class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # if(len(s)==1):
        #     return 1
        # r = len(s)-1
        # chore = s[-1]
        # counter = 0
        # while(chore==' '): #this and
        #     r = r - 1      #this together not good maybe do while?
        #     chore = s[r]
        # if(r==0):
        #     return 1
        # while (r>0 and s!=' '):
        #     if(s[r]==' '):
        #         #counter = counter + 1
        #         break
        #     counter = counter + 1
        #     r = r - 1
        # return counter
        index = len(s)-1
        counter = 0
        while(s[index]==' '):
            index = index - 1
        while(s[index]!=' ' and index>=0):
            counter = counter + 1
            index = index - 1
        return counter    