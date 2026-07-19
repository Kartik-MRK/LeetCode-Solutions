<h2><a href="https://leetcode.com/problems/n-th-tribonacci-number">0000. N Th Tribonacci Number</a></h2>

<p>The Tribonacci sequence T<sub>n</sub> is defined as follows:&nbsp;</p>

<p>T<sub>0</sub> = 0, T<sub>1</sub> = 1, T<sub>2</sub> = 1, and T<sub>n+3</sub> = T<sub>n</sub> + T<sub>n+1</sub> + T<sub>n+2</sub> for n &gt;= 0.</p>

<p>Given <code>n</code>, return the value of T<sub>n</sub>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> n = 4
<strong>Output:</strong> 4
<strong>Explanation:</strong>
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> n = 25
<strong>Output:</strong> 1389537
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 37</code></li>
	<li>The answer is guaranteed to fit within a 32-bit integer, ie. <code>answer &lt;= 2^31 - 1</code>.</li>
</ul>


---

# 🛍️ N-Th-Tribonacci-Number | Explained

## Approach 1: Iterative Tribonacci Calculation
### Intuition
The core idea behind this approach is to utilize a bottom-up dynamic programming strategy, where each Tribonacci number is calculated as the sum of the three preceding ones, thus avoiding redundant calculations and optimizing performance. This approach works by iteratively computing and storing the necessary Tribonacci numbers until the nth number is reached.

### Approach
The algorithm starts by initializing the first three Tribonacci numbers (0, 1, and 1) and then iteratively calculates the next numbers in the sequence, updating the previous three numbers at each step.

### Detailed Code Analysis
Let's break down the code line-by-line:
- `one`, `two`, and `three` are initialized to store the last three calculated Tribonacci numbers, starting with the first three numbers in the sequence.
- The base case `if n <= 2` checks if the desired Tribonacci number is one of the first three numbers (0, 1, and 1). If `n` is 0, it returns 0; otherwise, it returns 1.
- The `for` loop iterates from `i = 3` to `n` (inclusive) and at each step calculates the next Tribonacci number as the sum of the last three numbers (`one + two + three`).
- To avoid overwriting the values of `one` and `two` before they are used in the calculation, temporary variables `temp1` and `temp2` are used to store the current values of `three` and `two` before updating `three` with the newly calculated Tribonacci number.
- Finally, the values of `two` and `one` are updated with the stored temporary values `temp1` and `temp2`, respectively, effectively shifting the window of the last three calculated Tribonacci numbers.

### Code
```python
class Solution:
    def tribonacci(self, n: int) -> int:
        one = 0
        two = 1
        three = 1
        if n <= 2:
            if n:
                return 1
            else:
                return 0
        for i in range(3, n + 1):
            temp1 = three
            temp2 = two
            three = one + two + three
            two = temp1
            one = temp2
        return three
```
### Complexity
- **Time:** O(n) - This is because the algorithm iterates `n` times to calculate the nth Tribonacci number, performing a constant amount of work at each iteration.
- **Space:** O(1) - The space complexity is constant because the algorithm uses a fixed amount of space to store the last three calculated Tribonacci numbers, regardless of the input size `n`.

## 🕵️‍♂️ Follow-up Questions (Optional)
Common follow-up questions for this pattern include:
- How would you modify the solution to calculate the nth Fibonacci number (a sequence where each number is the sum of the two preceding ones) instead of the nth Tribonacci number?
  - Answer: You would only need to keep track of the last two numbers instead of three and adjust the calculation accordingly.
- Can you solve this problem using a recursive approach with memoization?
  - Answer: Yes, you can solve it by using a recursive function that calculates the nth Tribonacci number and stores the results of subproblems to avoid redundant calculations.