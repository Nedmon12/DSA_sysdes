class Solution:
    def isPalindrome(self, s: str) -> bool:
        # define fucntion to clean strings
        l , r = 0, len(s) - 1
        while (l<r):
            if(not(s[l].isalnum())):
                l = l + 1
                continue
            if (not(s[r].isalnum())):
                r = r - 1
                continue
            if (s[l].isalnum() and s[r].isalnum()):
                if (s[l].lower()!=s[r].lower()):
                    return False
            l = l+1
            r = r-1
        return True
    

    ### 