<h2><a href="https://leetcode.com/problems/reverse-linked-list">206. Reverse Linked List</a></h2>

<p>Given the <code>head</code> of a singly linked list, reverse the list, and return <em>the reversed list</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg" style="width: 542px; height: 222px;">
<pre><strong>Input:</strong> head = [1,2,3,4,5]
<strong>Output:</strong> [5,4,3,2,1]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg" style="width: 182px; height: 222px;">
<pre><strong>Input:</strong> head = [1,2]
<strong>Output:</strong> [2,1]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> head = []
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is the range <code>[0, 5000]</code>.</li>
	<li><code>-5000 &lt;= Node.val &lt;= 5000</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> A linked list can be reversed either iteratively or recursively. Could you implement both?</p>


---

# 🛍️ Reverse-Linked-List | Explained

## Approach 1 (Iterative Reversal)
### Intuition
The core idea revolves around iterating through the linked list and reversing the direction of the pointers by keeping track of the previous node, effectively flipping the list's direction. This approach leverages a simple, iterative method to achieve the reversal without using recursion.
### Approach
The algorithm starts by initializing three pointers: `prev`, `temp`, and `tmp`. It iterates through the list, updating the `next` pointer of each node to point to the previous node (`prev`), effectively reversing the link. It then moves the `prev` and `temp` pointers one step forward in each iteration until it reaches the end of the list.
### Code
```python
prev = None
temp = head
while temp:
    tmp = temp.next
    temp.next = prev
    prev = temp
    temp = tmp
return prev
```
### Complexity
- Time: O(n), where n is the number of nodes in the linked list, because we are traversing the list once.
- Space: O(1), as we are using a constant amount of space to store the pointers, regardless of the size of the input list.

## 🕵️‍♂️ Follow-up Questions (Optional)
Some common follow-up questions for this pattern include:
1. How would you implement this using recursion?
2. Can you optimize this solution further for very large linked lists?

To answer these questions:
1. To implement using recursion, you would recursively traverse the list, reversing the links as you return from each recursive call.
2. The provided iterative solution already achieves optimal runtime and space complexity (O(n) time and O(1) space), making it suitable for large linked lists. However, for extremely large lists that may not fit in memory, a more complex approach involving disk-based storage or processing the list in chunks might be necessary.

1. **Core Intuition**: The algorithm iterates through the linked list, reversing the direction of the pointers to flip the list's direction, utilizing a simple iterative method. This approach leverages three pointers to keep track of the previous node and the current node, effectively reversing the links.
2. **Complexity Analysis**:
   * Time complexity: O(n), where n is the number of nodes in the linked list, because we traverse the list once.
   * Space complexity: O(1), as we use a constant amount of space to store the pointers, regardless of the input size. 
   Key justifications:
     * Time complexity is linear due to the single pass through the list.
     * Space complexity is constant because we only use a fixed amount of space for the pointers.
3. **Critical Optimizations**: The provided solution achieves optimal runtime (O(n)) and space (O(1)) complexity, making it efficient for reversing linked lists of varying sizes. No further microscopic micro-optimizations are necessary for this iterative approach, as it already meets the optimal boundaries for both time and space complexity.