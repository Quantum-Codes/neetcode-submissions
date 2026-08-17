import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # okay so at every nums[i], we can either start a new seq or improve 
        # [9 1 4 2 3 3 7]
        # [9]
        # [1 4 7]
        # [1 2 3 3 7]
        # max is the bottom. 
        # we can rather try overwriting the moment we get a better val.
        # put it in correct spot so we can binary search and find where to write
        
        temp = [] 
        for item in nums:
            if not temp or item > temp[-1]:
                temp.append(item) # start one if not temp or extend
                continue
            # this means we need to overwrite at some pos.
            write_index = bisect.bisect_left(temp, item)
            temp[write_index] = item
        
        return len(temp)