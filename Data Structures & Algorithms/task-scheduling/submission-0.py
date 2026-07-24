class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(int)
        max_count = 0
        max_num = 0
        for task in tasks:
            freq[task] += 1
            if max_count == freq[task]:
                max_num += 1
            elif freq[task] > max_count:
                max_num = 1
                max_count = freq[task]
        

        # need (maxcount - 1) * n number of gaps and maxcount number of places
        # (maxcount - 1) * n + maxcount = (n+1)maxcount-n
        # lower bound = (n + 1) * max_count - n
        # correct if len(freq) <= n and max is uniquely max
        # if not uniquely max then we just do: (Add maxnum-1)

        # lower bound = (n + 1) * (max_count + 1) + max_num
        # theres another lowerbound: len(tasks). need these if its a stallfree exec
        # we return the higher of the lowerbounds

        return max(len(tasks), (n+1)*(max_count-1)+max_num)