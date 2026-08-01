<h2><a href="https://leetcode.com/problems/predict-the-winner">486. Predict the Winner</a></h2>

<p>You are given an integer array <code>nums</code>. Two players are playing a game with this array: player 1 and player 2.</p>

<p>Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of <code>0</code>. At each turn, the player takes one of the numbers from either end of the array (i.e., <code>nums[0]</code> or <code>nums[nums.length - 1]</code>) which reduces the size of the array by <code>1</code>. The player adds the chosen number to their score. The game ends when there are no more elements in the array.</p>

<p>Return <code>true</code> if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, and you should also return <code>true</code>. You may assume that both players are playing optimally.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,5,2]
<strong>Output:</strong> false
<strong>Explanation:</strong> Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return false.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,5,233,7]
<strong>Output:</strong> true
<strong>Explanation:</strong> Player 1 first chooses 1. Then player 2 has to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 20</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>7</sup></code></li>
</ul>


---

# 🛍️ Predict-the-Winner | Explained

## Approach 1: Recursive Depth-First Search
### Intuition
The core idea behind this approach is to simulate the game by recursively exploring all possible moves for both players. The algorithm uses a depth-first search (DFS) strategy to traverse the game tree, considering all possible scenarios and determining the outcome based on the scores of the two players. This approach works by leveraging the recursive nature of the game, where each player's decision is dependent on the previous state of the game.

### Algorithm Visualized
```mermaid
graph LR
    A[Start Game] -->|Player 1|> B[Choose Left or Right]
    B -->|Left|> C[Player 2 Turn]
    B -->|Right|> D[Player 2 Turn]
    C -->|Choose Left or Right|> E[Game Continues]
    D -->|Choose Left or Right|> E
    E -->|Base Case: No More Moves|> F[Return Result]
```

### Approach
The approach involves recursively calling the `dfs` function for each possible move, considering both players' turns. The function takes the current state of the game, including the left and right indices, the scores of both players, and the current turn. The base case for the recursion is when there are no more moves left, at which point the function returns the result based on the scores.

### Detailed Code Analysis
The code starts by initializing the scores of both players to 0. The `dfs` function is then called with the initial state of the game, including the left and right indices (0 and `len(nums) - 1`, respectively), the scores of both players (0), and the current turn (1 for Player 1). The `dfs` function recursively calls itself for each possible move, considering both players' turns. The function uses a recursive OR operator (`or`) for Player 1's turn and a recursive AND operator (`and`) for Player 2's turn. This ensures that Player 1 will choose a move that guarantees a win, while Player 2 will choose a move that forces a draw or a loss for Player 1.

### Code
```python
from collections import deque

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        p1 = 0
        p2 = 0

        def dfs(left, right, p1, p2, turn):
            if left > right:
                if p1 >= p2:
                    return True
                else:
                    return False
            if turn == 1:
                return dfs(left + 1, right, p1 + nums[left], p2, 2) or dfs(left, right - 1, p1 + nums[right], p2, 2)
            elif turn == 2:
                return dfs(left + 1, right, p1, p2 + nums[left], 1) and dfs(left, right - 1, p1, p2 + nums[right], 1)

        return True if dfs(0, len(nums) - 1, 0, 0, 1) else False
```

### Complexity
- **Time:** O(2^n), where n is the number of elements in the input array. This is because the algorithm recursively explores all possible moves for both players, resulting in an exponential number of function calls.
- **Space:** O(n), where n is the maximum depth of the recursion call stack. This is because the algorithm uses recursive function calls to traverse the game tree, and the maximum depth of the recursion call stack is proportional to the number of elements in the input array.

## 🕵️‍♂️ Follow-up Questions (Optional)
1. Can this approach be optimized to improve performance? 
 Answer: Yes, this approach can be optimized using memoization or dynamic programming to store the results of sub-problems and avoid redundant calculations.
2. How does the algorithm handle the case where the input array is empty? 
 Answer: The algorithm will return False for an empty input array, as there are no moves to make and Player 1 cannot guarantee a win.