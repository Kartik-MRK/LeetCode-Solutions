<h2><a href="https://leetcode.com/problems/concatenation-of-array">1929. Concatenation of Array</a></h2>

<p>Given an integer array <code>nums</code> of length <code>n</code>, you want to create an array <code>ans</code> of length <code>2n</code> where <code>ans[i] == nums[i]</code> and <code>ans[i + n] == nums[i]</code> for <code>0 &lt;= i &lt; n</code> (<strong>0-indexed</strong>).</p>

<p>Specifically, <code>ans</code> is the <strong>concatenation</strong> of two <code>nums</code> arrays.</p>

<p>Return <em>the array </em><code>ans</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,1]
<strong>Output:</strong> [1,2,1,1,2,1]
<strong>Explanation:</strong> The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,3,2,1]
<strong>Output:</strong> [1,3,2,1,1,3,2,1]
<strong>Explanation:</strong> The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


---

# 🛍️ Concatenation-of-Array | Explained

## Approach 1 (Modular Concatenation)
### Intuition
The algorithmic strategy used here is to create a new list that is the concatenation of the input list with itself, utilizing the modulo operator to efficiently handle indexing and avoid explicit list concatenation. This intuition can be likened to a conveyor belt that seamlessly stitches together two instances of a production line, represented by the input list.
### Approach
The approach involves iterating over a range that is twice the length of the input list. For each index in this range, the corresponding element from the input list is selected using the modulo operator to ensure the index wraps around to the start of the list when it exceeds the list's length.
### Code
```python
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(2 * n):
            ans.append(nums[i % n])
        return ans
```
### Complexity
- Time: O(n)
- Space: O(n)
  * Justification:
    + Time complexity is O(n) because the algorithm iterates over the range of twice the length of the input list, resulting in a linear time complexity.
    + Space complexity is O(n) because the algorithm creates a new list that is twice the size of the input list.

## 🕵️‍♂️ Follow-up Questions (Optional)
Common follow-up questions for this pattern might include:
1. How would you optimize the space complexity if the input list is extremely large and memory is a concern?
   - Answer: Consider using a generator or an iterator to lazily yield the elements of the concatenated list instead of storing them in memory all at once.
2. Can you achieve the same result using list slicing and concatenation?
   - Answer: Yes, the same result can be achieved with list slicing and concatenation, but this approach may be less efficient for large lists due to the overhead of creating temporary lists.

# 💡 Solution Insights
1. **Core Intuition**: The algorithm efficiently creates a concatenated list by utilizing the modulo operator to cycle through the input list, effectively "stitching" two instances of the list together. This approach eliminates the need for explicit list concatenation.
2. **Complexity Analysis**:
   * Time Complexity: O(n), where n is the length of the input list. This is because the algorithm iterates over the range of twice the length of the input list.
   * Space Complexity: O(n), where n is the length of the input list. This is because the algorithm creates a new list that is twice the size of the input list.
3. **Critical Optimizations**: The provided solution achieves optimal runtime boundaries with a time complexity of O(n) and is quite efficient. However, for extremely large input lists where memory is a concern, using a generator or iterator to lazily yield elements could provide a microscopic micro-optimization in terms of space complexity.