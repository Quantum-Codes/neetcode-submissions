class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) # O(n) space and time conversion
        longest_streak = 0
        
        for num in num_set:
            # Check if 'num' is the START of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # Keep counting up as long as the next number exists
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                    
                longest_streak = max(longest_streak, current_streak)
                
        return longest_streak