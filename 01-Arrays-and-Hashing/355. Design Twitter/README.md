<h2><a href="https://leetcode.com/problems/design-twitter">355. Design Twitter</a></h2>

<p>Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the <code>10</code> most recent tweets in the user's news feed.</p>

<p>Implement the <code>Twitter</code> class:</p>

<ul>
	<li><code>Twitter()</code> Initializes your twitter object.</li>
	<li><code>void postTweet(int userId, int tweetId)</code> Composes a new tweet with ID <code>tweetId</code> by the user <code>userId</code>. Each call to this function will be made with a unique <code>tweetId</code>.</li>
	<li><code>List&lt;Integer&gt; getNewsFeed(int userId)</code> Retrieves the <code>10</code> most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be <strong>ordered from most recent to least recent</strong>.</li>
	<li><code>void follow(int followerId, int followeeId)</code> The user with ID <code>followerId</code> started following the user with ID <code>followeeId</code>.</li>
	<li><code>void unfollow(int followerId, int followeeId)</code> The user with ID <code>followerId</code> started unfollowing the user with ID <code>followeeId</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input</strong>
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
<strong>Output</strong>
[null, null, [5], null, null, [6, 5], null, [5]]

<strong>Explanation</strong>
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -&gt; [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -&gt; [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -&gt; [5], since user 1 is no longer following user 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= userId, followerId, followeeId &lt;= 500</code></li>
	<li><code>0 &lt;= tweetId &lt;= 10<sup>4</sup></code></li>
	<li>All the tweets have <strong>unique</strong> IDs.</li>
	<li>At most <code>3 * 10<sup>4</sup></code> calls will be made to <code>postTweet</code>, <code>getNewsFeed</code>, <code>follow</code>, and <code>unfollow</code>.</li>
	<li>A user cannot follow himself.</li>
</ul>


---

# 🛍️ Design-Twitter | Explained

The provided solution implements a Twitter-like system with post, follow, and unfollow functionality. Here's a breakdown of the approach:

## Approach 1 (Optimized)
### Intuition
The core idea behind this approach is to utilize a combination of data structures (default dictionaries, sets, and heaps) to efficiently manage user posts, followers, and news feeds. This strategy works by leveraging the strengths of each data structure: default dictionaries for storing user posts, sets for tracking followers, and heaps for efficiently retrieving the most recent posts.

### Approach
The algorithm can be broken down into three primary components:
1. **Post management**: When a user posts a tweet, the system stores the post with a unique timestamp and tweet ID.
2. **Follower management**: When a user follows another user, the system adds the followee to the follower's set of followees.
3. **News feed retrieval**: When a user retrieves their news feed, the system constructs a heap of the most recent posts from the user's followees and their own posts, then returns the top 10 posts.

### Detailed Code Analysis
The solution begins by initializing the necessary data structures:
```python
self.follower = defaultdict(set)
self.count = 0
self.post = defaultdict(list)
```
*   `self.follower` stores the followers for each user, represented as a set to ensure efficient insertion and removal of followees.
*   `self.count` serves as a timestamp for posts, incremented for each new post.
*   `self.post` stores the posts for each user, represented as a list to maintain the order of posts.

When a user posts a tweet, the system stores the post with a unique timestamp and tweet ID:
```python
def postTweet(self, userId: int, tweetId: int) -> None:
    if userId not in self.post:
        self.post[userId] = []
    self.post[userId].append([self.count, tweetId])
    self.count -= 1
```
*   The post is appended to the user's list of posts with the current timestamp (`self.count`) and tweet ID.
*   The timestamp (`self.count`) is decremented to ensure that newer posts have a lower timestamp.

When a user follows another user, the system adds the followee to the follower's set of followees:
```python
def follow(self, followerId: int, followeeId: int) -> None:
    self.follower[followerId].add(followeeId)
```
*   The followee is added to the follower's set of followees.

When a user unfollows another user, the system removes the followee from the follower's set of followees:
```python
def unfollow(self, followerId: int, followeeId: int) -> None:
    if followerId in self.follower:
        self.follower[followerId].remove(followeeId)
```
*   The followee is removed from the follower's set of followees if the follower exists in the `self.follower` dictionary.

When a user retrieves their news feed, the system constructs a heap of the most recent posts from the user's followees and their own posts:
```python
def getNewsFeed(self, userId: int) -> List[int]:
    res = []
    minheap = []
    self.follower[userId].add(userId)
    for followeeId in self.follower[userId]:
        if self.post[followeeId]:
            index = len(self.post[followeeId]) - 1
            count, tweetId = self.post[followeeId][index]
            minheap.append([count, tweetId, followeeId, index - 1])
    heapq.heapify(minheap)

    while minheap and len(res) < 10:
        count, tweetId, followeeId, index = heapq.heappop(minheap)
        res.append(tweetId)
        if index >= 0:
            count, tweetId = self.post[followeeId][index]
            heapq.heappush(minheap, [count, tweetId, followeeId, index - 1])

    return res
```
*   The system adds the user to their own set of followees to include their own posts in the news feed.
*   A heap (`minheap`) is constructed with the most recent posts from the user's followees and their own posts.
*   The heap is populated with tuples containing the post's timestamp, tweet ID, followee ID, and the index of the previous post for each followee.
*   The heap is heapified to maintain the heap property.
*   The system pops the most recent post from the heap, adds it to the result list, and pushes the next post from the same followee back into the heap until the result list has 10 posts or the heap is empty.

### Code
The specific code snippet for this approach is the entire provided solution.

### Complexity
- Time: 
    *   `postTweet`: O(1) because appending to a list takes constant time.
    *   `follow`: O(1) because adding an element to a set takes constant time.
    *   `unfollow`: O(1) because removing an element from a set takes constant time.
    *   `getNewsFeed`: O(n log n) because heapifying the min-heap takes O(n log n) time, where n is the total number of posts from the user's followees and their own posts. Popping and pushing elements from/to the heap take O(log n) time each. Since this is done at most 10 times, the overall time complexity remains O(n log n).
- Space: 
    *   O(n) for storing the posts, followers, and the min-heap, where n is the total number of posts and followees.

## 🕵️‍♂️ Follow-up Questions (Optional)
Some common interviewer follow-up questions for this pattern include:
1.  How would you handle a large number of users and posts, potentially exceeding the memory capacity of a single machine?
    *   Answer: You can use a distributed database or a data sharding approach to store the data across multiple machines, ensuring that each machine handles a manageable subset of the data.
2.  How would you optimize the `getNewsFeed` method to improve performance, considering the potential for a large number of followees and posts?
    *   Answer: You can use a more efficient data structure, such as a balanced binary search tree or a skip list, to store the posts and followees. Additionally, you can implement a caching mechanism to store the most recent posts for each user, reducing the need to reconstruct the min-heap for each news feed request.