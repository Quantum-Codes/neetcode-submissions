class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # need to diff all words with each other
        # N^2 comparison between words
        # M ops to compare 2 words
        # O(M * N^2)
        # depth of search min = diff between begin and endWord. 
        # this is allowed acc to constraints. lets find better

        # can bucket patterns O(M) per 


        if endWord not in wordList:
            return 0
        
        # O(m**2*n)
        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adj[pattern].append(word)

        # now bfs to find shortest path
        queue = deque([(beginWord, 1)])
        visited = set()
        while queue:
            cur_word, level = queue.popleft()
            if cur_word in visited:
                continue 
            visited.add(cur_word)

            if cur_word == endWord:
                return level

            # gen pattern
            for i in range(len(cur_word)):
                pattern = cur_word[:i] + "*" + cur_word[i+1:]
                queue.extend([(item, level+1) for item in adj[pattern]])
                
        return 0

            
        