class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.posts = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.posts[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        posts = []
        counters = defaultdict(lambda: -1)
        self.following[userId].add(userId) #not damaging to any function here
        while len(posts) < 10:
            max_pass_id = -1
            max_pass_time = 0
            for follow in self.following[userId]:
                if len(self.posts[follow]) < -counters[follow]:
                    continue # out of bounds
                if max_pass_time < self.posts[follow][counters[follow]][0]:
                    max_pass_id = follow
                    max_pass_time = self.posts[follow][counters[follow]][0]
            
            if max_pass_id == -1:
                break # no more posts
            posts.append(self.posts[max_pass_id][counters[max_pass_id]][1])
            counters[max_pass_id] -= 1
        return posts


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
