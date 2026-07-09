<h2><a href="https://leetcode.com/problems/keys-and-rooms">841. Keys and Rooms</a></h2>

<p>There are <code>n</code> rooms labeled from <code>0</code> to <code>n - 1</code>&nbsp;and all the rooms are locked except for room <code>0</code>. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.</p>

<p>When you visit a room, you may find a set of <strong>distinct keys</strong> in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.</p>

<p>Given an array <code>rooms</code> where <code>rooms[i]</code> is the set of keys that you can obtain if you visited room <code>i</code>, return <code>true</code> <em>if you can visit <strong>all</strong> the rooms, or</em> <code>false</code> <em>otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> rooms = [[1],[2],[3],[]]
<strong>Output:</strong> true
<strong>Explanation:</strong> 
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> rooms = [[1,3],[3,0,1],[2],[0]]
<strong>Output:</strong> false
<strong>Explanation:</strong> We can not enter room number 2 since the only key that unlocks it is in that room.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == rooms.length</code></li>
	<li><code>2 &lt;= n &lt;= 1000</code></li>
	<li><code>0 &lt;= rooms[i].length &lt;= 1000</code></li>
	<li><code>1 &lt;= sum(rooms[i].length) &lt;= 3000</code></li>
	<li><code>0 &lt;= rooms[i][j] &lt; n</code></li>
	<li>All the values of <code>rooms[i]</code> are <strong>unique</strong>.</li>
</ul>


---

# 🛍️ Keys-and-Rooms | Explained

## Approach 1 (Breadth-First Search)
### Intuition
The core idea behind this approach is to utilize a Breadth-First Search (BFS) algorithm to traverse through the rooms, exploring each room and its corresponding keys. This approach works because it ensures that we visit each room and its adjacent rooms in a systematic and efficient manner, allowing us to determine if we can visit all rooms.

### Approach
The algorithmic breakdown is as follows:
1. Initialize a visited array to keep track of the rooms we've visited.
2. Start by visiting the first room (room 0) and add it to the queue.
3. While the queue is not empty, dequeue a room and mark it as visited.
4. For each key in the current room, if the corresponding room has not been visited, add it to the queue.
5. After visiting all rooms, check if there are any unvisited rooms by iterating through the visited array. If all rooms have been visited, return True; otherwise, return False.

### Detailed Code Analysis
Let's dive into the code:
```python
from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)  # Get the total number of rooms
        visited = [False] * n  # Initialize the visited array
        queue = deque([0])  # Initialize the queue with room 0
        # for ele in rooms[0]:  # This line is commented out, but it seems to be an older approach
        #     queue.append(ele)
        
        while queue:  # While the queue is not empty
            room = queue.popleft()  # Dequeue a room
            visited[room] = True  # Mark the room as visited
            visited[0] = True  # This line seems redundant, as room 0 should already be marked as visited
            
            for ele in rooms[room]:  # For each key in the current room
                if not visited[ele]:  # If the corresponding room has not been visited
                    queue.append(ele)  # Add it to the queue
                    
        for ele in visited:  # After visiting all rooms, check if there are any unvisited rooms
            if not ele:  # If an unvisited room is found
                return False  # Return False
        return True  # If all rooms have been visited, return True
```
The choice of using a queue data structure is efficient for BFS, as it allows us to easily add and remove rooms from the front and back of the queue.

### Code
```python
from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        queue = deque([0])
        
        while queue:
            room = queue.popleft()
            visited[room] = True
            
            for ele in rooms[room]:
                if not visited[ele]:
                    queue.append(ele)
                    
        for ele in visited:
            if not ele:
                return False
        return True
```
### Complexity
- Time: O(n + m), where n is the number of rooms and m is the total number of keys across all rooms. This is because we visit each room once and iterate through all the keys in each room.
- Space: O(n), as we need to store the visited array and the queue, which can contain up to n rooms.

## 🕵️‍♂️ Follow-up Questions (Optional)
Some potential follow-up questions for this problem include:
* How would you optimize the code to handle a large number of rooms and keys?
* What if the input is not a list of lists, but rather a graph data structure? How would you modify the code to accommodate this?

To directly address the user's custom instructions:

1. **Core Intuition**: The algorithmic strategy used is Breadth-First Search (BFS) to traverse through the rooms and their corresponding keys. This approach ensures a systematic and efficient exploration of all rooms.
2. **Complexity Analysis**:
    * Time complexity: O(n + m), where n is the number of rooms and m is the total number of keys across all rooms.
    * Space complexity: O(n), as we need to store the visited array and the queue.
    Justification:
        + Time complexity is O(n + m) because we visit each room once and iterate through all the keys in each room.
        + Space complexity is O(n) because we need to store the visited array and the queue, which can contain up to n rooms.
3. **Critical Optimizations**: The current approach achieves optimal runtime/space boundaries, as it uses a BFS algorithm to traverse the rooms and their corresponding keys in a systematic and efficient manner. However, microscopic micro-optimizations could include using a more efficient data structure for the queue or visited array, but these optimizations would likely have a negligible impact on performance.