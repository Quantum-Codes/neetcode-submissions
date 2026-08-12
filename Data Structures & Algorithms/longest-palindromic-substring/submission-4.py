class Solution:
    def longestPalindrome(self, s: str) -> str:
        soln = ""
        for c in range(len(s)):

            # odd len palindrome
            r = 0 # radius
            while c-r>=0 and c+r<len(s) and s[c-r] == s[c+r]:
                r += 1
            
            soln = max(soln, s[c-r+1:c+r], key = len)

            # even len palindrome
            left, right = c, c+1
            while left>=0 and right<len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            if (left+1<len(s) and s[left+1] == s[right-1]):
                soln = max(soln, s[left+1: right], key=len)
        
        return soln