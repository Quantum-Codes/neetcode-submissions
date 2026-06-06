class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0
        s_map = Counter()
        t_map = Counter(t)
        matches = 52 - len(set(t)) # the zero occurances match already

        best_left = -1000000000
        best_right = -1

        for right in range(len(s)):
            char = s[right]
            if s_map[char] >= t_map[char]:
                matches -= 1 # at end it should be incremented by 0 total. so reduce here and increase later to reduce number of conditions
            s_map[char] += 1
            if s_map[char] >= t_map[char]:
                matches += 1

            while matches == 52:
                # got a window, shrink from left
                char_leaving = s[left]
                # will not match anymore if it were equal before. this happens only once per window, after which while breaks
                if s_map[char_leaving] == t_map[char_leaving]:
                    matches -= 1

                    if right - left < best_right - best_left:
                        best_left = left
                        best_right = right

                s_map[char_leaving] -= 1
                left += 1

                # purposely made it not match at end of loop so next iteration doesnt immediately match
        
        return s[best_left: best_right + 1]

            