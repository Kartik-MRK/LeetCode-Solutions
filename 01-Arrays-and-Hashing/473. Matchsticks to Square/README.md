<h2><a href="https://leetcode.com/problems/matchsticks-to-square">473. Matchsticks to Square</a></h2>

<p>You are given an integer array <code>matchsticks</code> where <code>matchsticks[i]</code> is the length of the <code>i<sup>th</sup></code> matchstick. You want to use <strong>all the matchsticks</strong> to make one square. You <strong>should not break</strong> any stick, but you can link them up, and each matchstick must be used <strong>exactly one time</strong>.</p>

<p>Return <code>true</code> if you can make this square and <code>false</code> otherwise.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/09/matchsticks1-grid.jpg" style="width: 253px; height: 253px;">
<pre><strong>Input:</strong> matchsticks = [1,1,2,2,2]
<strong>Output:</strong> true
<strong>Explanation:</strong> You can form a square with length 2, one side of the square came two sticks with length 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> matchsticks = [3,3,3,3,4]
<strong>Output:</strong> false
<strong>Explanation:</strong> You cannot find a way to form a square with all the matchsticks.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= matchsticks.length &lt;= 15</code></li>
	<li><code>1 &lt;= matchsticks[i] &lt;= 10<sup>8</sup></code></li>
</ul>


---

# 🛍️ Matchsticks-to-Square | Explained

## Approach 1: Depth-First Search with Pruning
### Intuition
The core idea is to utilize a depth-first search (DFS) strategy, sorting the matchsticks in descending order and pruning branches that exceed the target side length, ensuring an efficient exploration of possible combinations.
### Approach
The algorithm sorts the matchsticks in descending order, calculates the target side length, and then uses DFS to attempt to fill each side of the square. It prunes branches by skipping identical sides and avoiding additions that exceed the target side length.
### Code
```python
def makesquare(self, matchsticks: List[int]) -> bool:
    matchsticks.sort(reverse=True)
    n=len(matchsticks)
    if n<4:
        return False
    perimeter=sum(matchsticks)
    if perimeter%4!=0:
        return False
    side=perimeter//4

    def dfs(sides,count):
        if count==n:
            return True
        for i in range(4):    
            if i>0 and sides[i]==sides[i-1]:
                continue
            if sides[i]+matchsticks[count]<=side:
                sides[i]+=matchsticks[count]
                if dfs(sides,count+1):
                    return True
                sides[i]-=matchsticks[count]               
            if sides[i]==0:
                break
        return False
    return dfs([0,0,0,0],0)      
```
### Complexity
- Time: O(4^n) 
  * Justification:
    * The algorithm explores all possible combinations of matchsticks in the worst case.
    * The DFS function is called recursively for each of the 4 sides.
- Space: O(n)
  * Justification:
    * The maximum depth of the recursion tree is equal to the number of matchsticks (n).
    * The space used by the `sides` list and the recursive call stack is proportional to n.

## 📊 Analysis
1. **Core Intuition**: This algorithm employs a depth-first search strategy with pruning to efficiently find a combination of matchsticks that forms a square. The key idea is to sort the matchsticks in descending order and prune branches that exceed the target side length.
2. **Complexity Analysis**:
   * Time complexity: O(4^n)
   * Space complexity: O(n)
   * Justifications:
     + Time complexity is O(4^n) because in the worst-case scenario, the algorithm explores all possible combinations of matchsticks.
     + Space complexity is O(n) because the maximum depth of the recursion tree is equal to the number of matchsticks.
3. **Critical Optimizations**: The current approach achieves a significant optimization by sorting the matchsticks in descending order and pruning branches, which reduces the search space and improves the algorithm's efficiency. However, further microscopic optimizations might include using more advanced techniques like memoization or dynamic programming to store and reuse the results of subproblems, but these would add complexity to the code and may not provide substantial benefits for this specific problem.

## 🕵️‍♂️ Follow-up Questions (Optional)
Some potential follow-up questions for this problem include:
* How would you handle the case where the input array is very large? (Answer: You could consider using more advanced techniques like memoization or dynamic programming to store and reuse the results of subproblems.)
* Can you prove that the current approach is optimal in terms of time complexity? (Answer: The current approach has a time complexity of O(4^n), which is optimal for this problem because it must explore all possible combinations of matchsticks in the worst case.)