<h2><a href="https://leetcode.com/problems/kth-largest-element-in-an-array">215. Kth Largest Element in an Array</a></h2>

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <em>the</em> <code>k<sup>th</sup></code> <em>largest element in the array</em>.</p>

<p>Note that it is the <code>k<sup>th</sup></code> largest element in the sorted order, not the <code>k<sup>th</sup></code> distinct element.</p>

<p>Can you solve it without sorting?</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [3,2,1,5,6,4], k = 2
<strong>Output:</strong> 5
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [3,2,3,1,2,4,5,5,6], k = 4
<strong>Output:</strong> 4
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>


---

# 🛍️ Kth-Largest-Element-in-an-Array | Explained

## Approach 1 (Optimized)
### Intuition
The core idea behind this approach is to utilize a min-heap data structure to efficiently find the kth largest element in an array. By maintaining a heap of size k, we can ensure that the smallest element in the heap is always the kth largest element in the array. This approach works because the min-heap property allows us to easily remove the smallest element and replace it with a larger one, effectively "bubbling up" the largest elements to the top.
### Approach
The high-level logic flow of this approach is as follows:
1. Initialize an empty min-heap.
2. Iterate through the input array, and for each element:
   - If the heap is not full (i.e., its size is less than k), push the element onto the heap.
   - If the heap is full and the current element is larger than the smallest element in the heap, remove the smallest element from the heap and push the current element onto the heap.
3. After iterating through the entire array, the smallest element in the heap is the kth largest element.
### Detailed Code Analysis
Let's dive into the code block:
```python
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []  # Initialize an empty min-heap
        for ele in nums:  # Iterate through the input array
            if len(heap) < k:  # If the heap is not full
                heapq.heappush(heap, ele)  # Push the element onto the heap
            else:
                if heap[0] < ele:  # If the heap is full and the current element is larger than the smallest element
                    heapq.heappop(heap)  # Remove the smallest element from the heap
                    heapq.heappush(heap, ele)  # Push the current element onto the heap
        return heap[0]  # Return the smallest element in the heap (the kth largest element)
```
The code uses the `heapq` module to implement the min-heap, which provides an efficient way to push and pop elements while maintaining the heap property. The `heap` variable represents the min-heap, and the `ele` variable represents the current element being processed.
### Code
```python
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for ele in nums:
            if len(heap) < k:
                heapq.heappush(heap, ele)
            else:
                if heap[0] < ele:
                    heapq.heappop(heap)
                    heapq.heappush(heap, ele)
        return heap[0]
```
### Complexity
- Time: O(n log k), where n is the size of the input array. This is because we iterate through the array once, and for each element, we perform a heap operation (push or pop) that takes O(log k) time.
- Space: O(k), where k is the size of the heap. This is because we store at most k elements in the heap.

## 🕵️‍♂️ Follow-up Questions (Optional)
Some common follow-up questions for this pattern include:
- How would you optimize the solution for very large input arrays?
  Answer: One possible optimization is to use a more efficient heap implementation, such as a binary heap or a Fibonacci heap. Additionally, we could consider using a parallel or distributed algorithm to process the input array in parallel.
- What if the input array is sorted in ascending or descending order?
  Answer: If the input array is already sorted, we can simply return the kth element from the end (for ascending order) or the kth element from the beginning (for descending order). This would have a time complexity of O(1) and space complexity of O(1).

**Core Intuition**: The algorithmic strategy used is to maintain a min-heap of size k to efficiently find the kth largest element in an array. The min-heap property allows us to easily remove the smallest element and replace it with a larger one.
**Complexity Analysis**:
* Time: O(n log k)
  * Justification:
    + We iterate through the array once, which takes O(n) time.
    + For each element, we perform a heap operation (push or pop) that takes O(log k) time.
* Space: O(k)
  * Justification:
    + We store at most k elements in the heap.
**Critical Optimizations**: This approach achieves optimal runtime boundaries, as the time complexity of O(n log k) is the best we can achieve for this problem. However, there may be microscopic micro-optimizations possible, such as using a more efficient heap implementation or optimizing the code for specific input scenarios.