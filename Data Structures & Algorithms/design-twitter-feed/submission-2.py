class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.posts = [] # minheap
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        heapq.heappush_max(self.posts, (self.time, tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        # dupe heap and then pop
        heap = self.posts.copy() # O(N)
        posts = []
        while heap and len(posts) < 10:
            post = heapq.heappop_max(heap)
            if post[2] in self.following[userId] or post[2] == userId:
                posts.append(post[1])
        
        # Total O(NLOGN)
        
        return posts


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
