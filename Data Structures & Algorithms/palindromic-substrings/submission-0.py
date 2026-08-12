class Solution:
    def countSubstrings(self, s: str) -> int:
        soln = 0
        for c in range(len(s)):

            # odd len palindrome
            r = 0 # radius
            while c-r>=0 and c+r<len(s) and s[c-r] == s[c+r]:
                r += 1
                soln += 1
            
            # even len palindrome
            left, right = c, c+1
            while left>=0 and right<len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                soln += 1
            
        
        return soln