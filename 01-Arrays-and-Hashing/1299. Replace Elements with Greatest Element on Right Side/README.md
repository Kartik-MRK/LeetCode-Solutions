<h2><a href="https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side">1299. Replace Elements with Greatest Element on Right Side</a></h2>

<p>Given an array <code>arr</code>,&nbsp;replace every element in that array with the greatest element among the elements to its&nbsp;right, and replace the last element with <code>-1</code>.</p>

<p>After doing so, return the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> arr = [17,18,5,4,6,1]
<strong>Output:</strong> [18,6,6,6,1,-1]
<strong>Explanation:</strong> 
- index 0 --&gt; the greatest element to the right of index 0 is index 1 (18).
- index 1 --&gt; the greatest element to the right of index 1 is index 4 (6).
- index 2 --&gt; the greatest element to the right of index 2 is index 4 (6).
- index 3 --&gt; the greatest element to the right of index 3 is index 4 (6).
- index 4 --&gt; the greatest element to the right of index 4 is index 5 (1).
- index 5 --&gt; there are no elements to the right of index 5, so we put -1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> arr = [400]
<strong>Output:</strong> [-1]
<strong>Explanation:</strong> There are no elements to the right of index 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= arr[i] &lt;= 10<sup>5</sup></code></li>
</ul>


---

# 🛍️ Replace-Elements-with-Greatest-Element-on-Right-Side | Explained

## Approach 1 (Optimized)
### Intuition
This approach works by utilizing a single pass through the input array from right to left, effectively replacing each element with the maximum value to its right. The intuition behind this strategy is to maintain a running maximum of elements encountered so far from the right, which can be used to update each element in the array.
### Approach
The algorithm operates by starting from the end of the array and moving towards the beginning. It keeps track of the maximum element encountered so far from the right, which is used to replace the current element.
### Detailed Code Analysis
Let's break down the code:
- Line 3: `n=len(arr)` calculates the length of the input array, which is used to iterate over the array from right to left.
- Line 4: `maxele=-1` initializes the `maxele` variable to store the maximum element encountered so far from the right. It's initialized to -1, assuming the minimum possible integer value.
- Line 5: `for i in range(n-1,-1,-1)` starts a loop that iterates over the array from right to left.
- Line 6: `curr=maxele` stores the current maximum element encountered so far from the right in the `curr` variable.
- Line 7: `maxele=max(maxele,arr[i])` updates the `maxele` variable to be the maximum of the current `maxele` and the current element `arr[i]`.
- Line 8: `arr[i]=curr` replaces the current element `arr[i]` with the maximum element encountered so far from the right, which is stored in the `curr` variable.
### Code
```python
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        maxele=-1
        for i in range(n-1,-1,-1):
            curr=maxele
            maxele=max(maxele,arr[i])
            arr[i]=curr
        return arr
```
### Complexity
- Time: O(n), where n is the length of the input array. This is because the algorithm makes a single pass through the array from right to left.
- Space: O(1), excluding the space required for the output array. This is because the algorithm only uses a constant amount of space to store the `maxele` and `curr` variables.

## 💡 Core Strategy Insights
1. **Core Intuition**: The algorithm works by performing a single pass through the input array from right to left, maintaining a running maximum of elements encountered so far from the right to update each element.
2. **Complexity Analysis**:
  * Time: O(n), where n is the length of the input array, as the algorithm makes a single pass through the array.
  * Space: O(1), excluding the space required for the output array, as the algorithm uses a constant amount of space.
3. **Critical Optimizations**: The approach achieves optimal runtime and space boundaries, as it only requires a single pass through the input array and uses a constant amount of space. No further optimizations are needed.

## 🕵️‍♂️ Follow-up Questions (Optional)
Some potential follow-up questions for this problem include:
- How would you handle an empty input array?
- Can you modify the algorithm to replace elements with the minimum value to their right instead? 

Brief answers: 
- For an empty input array, the algorithm would simply return an empty array, as there are no elements to replace.
- To replace elements with the minimum value to their right, you can modify the algorithm to maintain a running minimum of elements encountered so far from the right instead of a running maximum.