class Solution:
    # O(n) 
    # len_window - max_freq > k
    # WE are returning max len_window. so we want that to be max.
    # for that to be max, and that above condition to fail, we gotta make max_freq max
    # and since we keep max_freq never decreasing, we never allow a lower len_window window even be considered, we reject smaller length windows.
    # we only need the max freq, so whenever we update dict we upadte rather than looping through all elements
    def find_max_freq(self, d: dict) -> int:
        return max(d.values())
        
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        freq = {}
        longest = 0
        maxFreq = 0
        for right in range(len(s)):
            freq.setdefault(s[right], 0)
            freq[s[right]] += 1
            maxFreq = max(maxFreq, freq[s[right]])    # ← cheap, only check the char we just added
            while (right - left + 1) - maxFreq > k:
                freq[s[left]] -= 1
                left += 1
                # NOTE: we deliberately do NOT update maxFreq here, even though its count dropped
            longest = max(longest, right - left + 1)
        return longest