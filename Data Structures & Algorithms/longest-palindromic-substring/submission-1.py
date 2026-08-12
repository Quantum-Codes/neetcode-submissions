class Solution:
    def longestPalindrome(self, s: str) -> str:
        string = "#" + "#".join(s) + "#"
        soln = ""
        for i in range(len(string)):
            j = 0
            while i >= j and i+j<len(string) and string[i-j] == string[i+j]:
                j += 1
            
            # len palindrome is j-1
            soln = max(soln, string[i-j+1: i+j], key=len)

        # a#b#b

        # now remove all hashtags
        translated = ""
        for c in soln:
            if c.isalnum():
                translated += c
        return translated