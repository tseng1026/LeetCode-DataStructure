# https://leetcode.com/problems/design-twitter/

class Twitter:
    def __init__(self):
        self.tweets = []
        self.followees = defaultdict(set)

    def postTweet(self, user_id: int, tweetId: int) -> None:
        self.tweets.append((user_id, tweetId))

    def getNewsFeed(self, user_id: int) -> List[int]:
        new_feeds = []
        idx, count = len(self.tweets) - 1, 0
        while idx >= 0 and count < 10:
            if self.tweets[idx][0] in self.followees[user_id] or \
                    self.tweets[idx][0] == user_id:
                new_feeds.append(self.tweets[idx][1])
                count += 1
            idx -= 1
        return new_feeds

    def follow(self, follower_id: int, followee_id: int) -> None:
        self.followees[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        self.followees[follower_id].discard(followee_id)
