<h2><a href="https://leetcode.com/problems/stone-game">877. Stone Game</a></h2>

<p>Alice and Bob play a game with piles of stones. There are an <strong>even</strong> number of piles arranged in a row, and each pile has a <strong>positive</strong> integer number of stones <code>piles[i]</code>.</p>

<p>The objective of the game is to end with the most stones. The <strong>total</strong> number of stones across all the piles is <strong>odd</strong>, so there are no ties.</p>

<p>Alice and Bob take turns, with <strong>Alice starting first</strong>. Each turn, a player takes the entire pile of stones either from the <strong>beginning</strong> or from the <strong>end</strong> of the row. This continues until there are no more piles left, at which point the person with the <strong>most stones wins</strong>.</p>

<p>Assuming Alice and Bob play optimally, return <code>true</code><em> if Alice wins the game, or </em><code>false</code><em> if Bob wins</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> piles = [5,3,4,5]
<strong>Output:</strong> true
<strong>Explanation:</strong> 
Alice starts first, and can only take the first 5 or the last 5.
Say she takes the first 5, so that the row becomes [3, 4, 5].
If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alice, so we return true.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> piles = [3,7,2,3]
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= piles.length &lt;= 500</code></li>
	<li><code>piles.length</code> is <strong>even</strong>.</li>
	<li><code>1 &lt;= piles[i] &lt;= 500</code></li>
	<li><code>sum(piles[i])</code> is <strong>odd</strong>.</li>
</ul>


---

# 🛍️ Stone-Game | Explained
## Approach 1: Dynamic Programming with Memoization
### Intuition
The core idea behind this approach is to use dynamic programming to store and reuse the results of subproblems, allowing us to efficiently determine the maximum score that can be achieved by either player. This approach works by recursively exploring all possible moves and their outcomes, while utilizing memoization to avoid redundant computations.

### Approach
The algorithm works as follows:
- It defines a recursive function `dfs` that takes two parameters, `l` and `r`, representing the current range of piles.
- It uses memoization to store the results of subproblems in a dictionary `dp`.
- For each subproblem, it checks if the result is already stored in `dp`. If it is, the stored result is returned.
- Otherwise, it calculates the maximum score that can be achieved by either player by recursively exploring all possible moves and their outcomes.
- The final result is determined by comparing the maximum score achieved by the first player with half of the total score.

### Detailed Code Analysis
Let's break down the code:
- Line 3: `dp={}` initializes an empty dictionary to store the results of subproblems.
- Line 4: `def dfs(l,r):` defines the recursive function `dfs`.
- Line 5: `if l>r: return 0` is the base case, where if the range `l` to `r` is empty, the function returns 0.
- Line 7: `if (l,r) in dp: return dp[(l,r)]` checks if the result of the current subproblem is already stored in `dp`.
- Line 9: `even=True if (r-l+1)%2==0 else False` determines if the current turn is even or odd.
- Lines 10-11: `left=piles[l] if even else 0` and `right=piles[r] if even else 0` calculate the score for the current turn.
- Line 12: `dp[(l,r)]=max(dfs(l+1,r)+left,dfs(l,r-1)+right)` calculates the maximum score that can be achieved by either player and stores the result in `dp`.
- Line 14: `return dfs(0,len(piles)-1)>sum(piles)//2` returns `True` if the first player can achieve a score greater than half of the total score.

### Code
```python
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            even = True if (r - l + 1) % 2 == 0 else False
            left = piles[l] if even else 0
            right = piles[r] if even else 0
            dp[(l, r)] = max(dfs(l + 1, r) + left, dfs(l, r - 1) + right)
            return dp[(l, r)]
        return dfs(0, len(piles) - 1) > sum(piles) // 2
```

### Complexity
- **Time:** O(n^2), where n is the number of piles. This is because in the worst-case scenario, the recursive function `dfs` is called for each possible subproblem, resulting in a time complexity of O(n^2).
- **Space:** O(n^2), where n is the number of piles. This is because the dictionary `dp` stores the results of all subproblems, resulting in a space complexity of O(n^2).

## 🕵️‍♂️ Follow-up Questions (Optional)
- What if the number of piles is extremely large? In this case, the current approach may not be efficient due to its high time and space complexity.
- How can we further optimize the current approach? One possible optimization is to use a more efficient data structure, such as a 2D array, to store the results of subproblems instead of a dictionary. However, this would require a more complex implementation.