class Solution:
    def isPalindrome(self, s: str) -> bool:
        # define fucntion to clean strings
        l , r = 0, len(s) - 1
        someflag = True
        if(len(s)%2==1):
            x = (len(s)//2) -1
            y = (len(s)//2) +1
        else :
            x = (len(s)/2) - 1
            y = (len(s)/2)
        while (l<r):
            if (l==x or r==y):
                return someflag
            if(not(s[l].isalnum())):
                l = l + 1
                continue
            if (not(s[r].isalnum())):
                r = r - 1
                continue
            if (s[l].isalnum() and s[r].isalnum()):
                if (s[l].lower()!=s[r].lower()):
                    someflag = False
                    # return False
            l = l+1
            r = r-1
        return True
    

    ### It works ig just some fine tunning
    

    ### 