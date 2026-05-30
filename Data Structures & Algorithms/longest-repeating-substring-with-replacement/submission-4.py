class Solution:
    def find_max_freq(self, d: dict) -> int:
        return max(d.values())
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        freq = {}
        longest = 0

        for right in range(len(s)):
            len_window = right - left + 1
            freq.setdefault(s[right], 0)
            freq[s[right]] += 1
            while len_window - self.find_max_freq(freq) > k:
                freq[s[left]] -= 1 
                left += 1
                len_window = right - left + 1

            longest = max(longest, len_window)
        
        return longest