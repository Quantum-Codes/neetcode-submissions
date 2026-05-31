import string

class Solution:
    def check_equal(self, a, b):
        # b is the t_map
        for char in string.ascii_lowercase + string.ascii_uppercase:
            if a[char] < b[char] and b[char] > 0:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        window = "a" * 1001
        s_map = Counter() 
        t_map = Counter(t)
        left = 0

        for right in range(len(s)):
            s_map[s[right]] += 1

            while self.check_equal(s_map, t_map):
                s_map[s[left]] -= 1
                left += 1
                window = min(window, s[left-1: right+1], key=len)
        
        if window == "a"*1001: return ""
        return window
