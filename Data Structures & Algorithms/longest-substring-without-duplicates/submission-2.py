class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        char_map = {}
        longest = 0
        for i in range(len(s)):
            if s[i] in char_map:                
                # clear map
                for j in range(left, char_map[s[i]]):
                    del char_map[s[j]]
                
                left = char_map[s[i]] + 1
            else:
                pass
            
            longest = max(longest, i - left + 1)
            char_map[s[i]] = i
        
        return longest
