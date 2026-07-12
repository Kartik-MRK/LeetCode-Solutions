<h2><a href="https://leetcode.com/problems/open-the-lock">752. Open the Lock</a></h2>

<p>You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: <code>'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'</code>. The wheels can rotate freely and wrap around: for example we can turn <code>'9'</code> to be <code>'0'</code>, or <code>'0'</code> to be <code>'9'</code>. Each move consists of turning one wheel one slot.</p>

<p>The lock initially starts at <code>'0000'</code>, a string representing the state of the 4 wheels.</p>

<p>You are given a list of <code>deadends</code> dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.</p>

<p>Given a <code>target</code> representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> deadends = ["0201","0101","0102","1212","2002"], target = "0202"
<strong>Output:</strong> 6
<strong>Explanation:</strong> 
A sequence of valid moves would be "0000" -&gt; "1000" -&gt; "1100" -&gt; "1200" -&gt; "1201" -&gt; "1202" -&gt; "0202".
Note that a sequence like "0000" -&gt; "0001" -&gt; "0002" -&gt; "0102" -&gt; "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> deadends = ["8888"], target = "0009"
<strong>Output:</strong> 1
<strong>Explanation:</strong> We can turn the last wheel in reverse to move from "0000" -&gt; "0009".
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
<strong>Output:</strong> -1
<strong>Explanation:</strong> We cannot reach the target without getting stuck.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= deadends.length &lt;= 500</code></li>
	<li><code>deadends[i].length == 4</code></li>
	<li><code>target.length == 4</code></li>
	<li>target <strong>will not be</strong> in the list <code>deadends</code>.</li>
	<li><code>target</code> and <code>deadends[i]</code> consist of digits only.</li>
</ul>


---

# 🛍️ Open-the-Lock | Explained

## Approach 1 (Breadth-First Search)
### Intuition
The core idea behind this approach is to treat the lock as a graph where each node represents a possible state of the lock, and the edges represent the possible moves (i.e., turning a dial up or down). By using a breadth-first search (BFS) algorithm, we can efficiently explore all possible states of the lock in a level-order manner. This approach works because it ensures that we visit the closest possible states to the initial state (i.e., "0000") before moving on to more distant states.
### Approach
The algorithm starts by initializing a queue with the initial state ("0000") and a turn count of 0. It then enters a loop where it dequeues the current state and turn count, checks if the current state is the target, and if so, returns the turn count. If not, it generates all possible next states by turning each dial up or down, checks if the next state has been visited before or is in the set of dead ends, and if not, adds it to the queue and marks it as visited.
### Detailed Code Analysis
Let's dive into the code block:
- Lines 1-3 import the necessary modules and define the `Solution` class.
- Line 4 converts the list of dead ends into a set for efficient lookups.
- Line 5 checks if the initial state ("0000") is in the set of dead ends, in which case it returns -1.
- Lines 7-8 initialize the `visited` set and the `queue` with the initial state and turn count.
- The while loop (lines 10-30) is the main BFS loop.
- Inside the loop, lines 11-13 dequeue the current state and turn count, and check if the current state is the target. If so, it returns the turn count.
- Lines 14-29 generate all possible next states by turning each dial up or down. For each next state, it checks if the next state has been visited before or is in the set of dead ends. If not, it adds the next state to the queue and marks it as visited.
### Code
```python
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        visited = set()
        queue = deque([["0000", 0]])
        visited.add("0000")
        while queue:
            curr, turn = queue.popleft()
            if curr == target:
                return turn
            for i in range(4):
                ele = list(curr)
                ele[i] = str((int(ele[i]) + 1) % 10)
                nxt = "".join(ele)
                if nxt not in dead and nxt not in visited:
                    visited.add(nxt)
                    queue.append([nxt, turn + 1])
                
                ele = list(curr)
                ele[i] = str((int(ele[i]) - 1) % 10)
                prev = "".join(ele)
                if prev not in dead and prev not in visited:
                    visited.add(prev)
                    queue.append([prev, turn + 1])
        return -1
```
### Complexity
- Time: O(10^4) because in the worst case, we need to visit all possible states of the lock, which is 10^4 (10 possible states for each of the 4 dials).
- Space: O(10^4) because in the worst case, we need to store all possible states of the lock in the `visited` set and the `queue`.

## 🕵️‍♂️ Follow-up Questions (Optional)
Some common follow-up questions for this pattern include:
- What if the lock has more than 4 dials? How would the algorithm change?
- How can we optimize the algorithm to use less space?

**Core Intuition**: The algorithm uses a breadth-first search strategy to efficiently explore all possible states of the lock. 
**Complexity Analysis**: 
* Time: O(10^4)
  * Justification:
    + We need to visit all possible states of the lock in the worst case.
    + There are 10 possible states for each of the 4 dials, resulting in 10^4 possible states.
* Space: O(10^4)
  * Justification:
    + We need to store all possible states of the lock in the `visited` set and the `queue` in the worst case.
    + There are 10 possible states for each of the 4 dials, resulting in 10^4 possible states.
**Critical Optimizations**: The algorithm achieves optimal runtime and space boundaries because it uses a breadth-first search strategy and stores visited states in a set to avoid duplicates. However, some microscopic micro-optimizations could include using a more efficient data structure for the `visited` set or using a more efficient algorithm for generating next states.