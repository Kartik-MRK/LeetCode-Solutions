<h2><a href="https://leetcode.com/problems/stone-game-iv">1510. Stone Game IV</a></h2>

<p>Alice and Bob take turns playing a game, with Alice starting first.</p>

<p>Initially, there are <code>n</code> stones in a pile. On each player's turn, that player makes a <em>move</em> consisting of removing <strong>any</strong> non-zero <strong>square number</strong> of stones in the pile.</p>

<p>Also, if a player cannot make a move, he/she loses the game.</p>

<p>Given a positive integer <code>n</code>, return <code>true</code> if and only if Alice wins the game otherwise return <code>false</code>, assuming both players play optimally.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> true
<strong>Explanation: </strong>Alice can remove 1 stone winning the game because Bob doesn't have any moves.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> n = 2
<strong>Output:</strong> false
<strong>Explanation: </strong>Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -&gt; 1 -&gt; 0).
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> n = 4
<strong>Output:</strong> true
<strong>Explanation:</strong> n is already a perfect square, Alice can win with one move, removing 4 stones (4 -&gt; 0).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
</ul>


---

# 🛍️ Stone-Game-IV | Explained

## Approach 1: Recursive Memoization
### Intuition
The core idea behind this approach is to utilize a recursive function with memoization to determine whether the current player can win the game. The algorithm works by recursively exploring all possible moves and storing the results of subproblems to avoid redundant calculations. This approach can be likened to a tree search, where each node represents a game state, and the algorithm prunes branches that lead to losing states.

### Approach
The algorithm starts by checking if the current state is a winning state (i.e., the remaining stones can be removed in a single turn). If not, it recursively explores all possible moves by removing a square number of stones. The algorithm uses memoization to store the results of subproblems, allowing it to avoid redundant calculations and improve performance.

### Detailed Code Analysis
The code defines a recursive function `backtrack` that takes the current number of stones `n` as input. The function first checks if the current state is a winning state by verifying if `n` is a perfect square. If it is, the function returns `True`, indicating that the current player can win. The function then checks if the result of the current state is already stored in the `dp` dictionary. If it is, the function returns the stored result. Otherwise, the function recursively explores all possible moves by iterating over all square numbers `k` that are less than or equal to the square root of `n`. For each move, the function checks if the opponent can win by recursively calling `backtrack` with the updated number of stones `n - k * k`. If the opponent cannot win, the function stores the result `True` in the `dp` dictionary and returns `True`. If all possible moves lead to the opponent winning, the function stores the result `False` in the `dp` dictionary and returns `False`.

### Code
```python
def winnerSquareGame(self, n: int) -> bool:
    dp = {}
    def backtrack(n):
        if n == 0:
            return False
        if math.sqrt(n) == int(math.sqrt(n)):
            return True
        if n in dp:
            return dp[n]
        for k in range(1, int(math.sqrt(n)) + 1):
            if not backtrack(n - k * k):
                dp[n] = True
                return dp[n]
        dp[n] = False
        return dp[n]
    return backtrack(n)
```

### Complexity
- **Time:** O(n sqrt(n)) - The time complexity is dominated by the recursive function `backtrack`, which has a time complexity of O(n sqrt(n)) due to the iteration over all square numbers up to the square root of `n`. The memoization using the `dp` dictionary reduces the number of recursive calls, but the overall time complexity remains O(n sqrt(n)).
- **Space:** O(n) - The space complexity is O(n) due to the storage of results in the `dp` dictionary, which can contain up to `n` entries in the worst case.

## Approach 2: Not Applicable
There is only one distinct approach in the provided code.

## 🕵️‍♂️ Follow-up Questions (Optional)
1. How can you optimize the algorithm to reduce the time complexity?
Answer: One possible optimization is to use a more efficient data structure, such as a bitset, to store the results of subproblems. Additionally, you can use a dynamic programming approach to iteratively fill in the `dp` array, rather than using recursive function calls.
2. How can you extend the algorithm to handle larger input values?
Answer: To handle larger input values, you can use a more efficient algorithm, such as a binary search approach, to find the largest square number that is less than or equal to `n`. Additionally, you can use a more efficient data structure, such as a trie or a suffix tree, to store the results of subproblems.