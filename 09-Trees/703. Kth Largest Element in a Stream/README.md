<h2><a href="https://leetcode.com/problems/kth-largest-element-in-a-stream">703. Kth Largest Element in a Stream</a></h2>

<p>You are part of a university admissions office and need to keep track of the <code>kth</code> highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.</p>

<p>You are tasked to implement a class which, for a given integer&nbsp;<code>k</code>, maintains a stream of test scores and continuously returns the&nbsp;<code>k</code>th highest test score&nbsp;<strong>after</strong>&nbsp;a new score has been submitted. More specifically, we are looking for the <code>k</code>th highest score in the sorted list of all scores.</p>

<p>Implement the&nbsp;<code>KthLargest</code> class:</p>

<ul>
	<li><code>KthLargest(int k, int[] nums)</code> Initializes the object with the integer <code>k</code> and the stream of test scores&nbsp;<code>nums</code>.</li>
	<li><code>int add(int val)</code> Adds a new test score&nbsp;<code>val</code> to the stream and returns the element representing the <code>k<sup>th</sup></code> largest element in the pool of test scores so far.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong><br>
<span class="example-io">["KthLargest", "add", "add", "add", "add", "add"]<br>
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[null, 4, 5, 5, 8, 8]</span></p>

<p><strong>Explanation:</strong></p>

<p>KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);<br>
kthLargest.add(3); // return 4<br>
kthLargest.add(5); // return 5<br>
kthLargest.add(10); // return 5<br>
kthLargest.add(9); // return 8<br>
kthLargest.add(4); // return 8</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong><br>
<span class="example-io">["KthLargest", "add", "add", "add", "add"]<br>
[[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[null, 7, 7, 7, 8]</span></p>

<p><strong>Explanation:</strong></p>
KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);<br>
kthLargest.add(2); // return 7<br>
kthLargest.add(10); // return 7<br>
kthLargest.add(9); // return 7<br>
kthLargest.add(9); // return 8</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= k &lt;= nums.length + 1</code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= val &lt;= 10<sup>4</sup></code></li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>add</code>.</li>
</ul>


---

# 🛍️ Kth-Largest-Element-in-a-Stream | Explained

## Approach 1 (Optimized)
### Intuition
The core idea behind this approach is to utilize a min-heap data structure to maintain the kth largest element in the stream. By keeping the heap size at most k, we ensure that the smallest element in the heap (i.e., the root) represents the kth largest element in the stream. This approach works because the min-heap allows us to efficiently remove and insert elements to maintain the desired size and ordering.

### Approach
The algorithmic breakdown can be summarized as follows:
1. Initialize a min-heap and set the target size to k.
2. Iterate through the initial list of numbers, adding the first k elements to the heap.
3. For each subsequent element in the list and new elements added to the stream:
   - If the heap size is less than k, add the new element to the heap.
   - If the new element is greater than or equal to the smallest element in the heap (i.e., the root), remove the smallest element and add the new element to the heap.

### Detailed Code Analysis
Let's dive into the code block:
```python
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # Initialize an empty min-heap
        self.heap = []
        # Store the target size (k)
        self.k = k
        # Iterate through the initial list of numbers
        for ele in nums[:k]:
            # Add the first k elements to the heap
            heapq.heappush(self.heap, ele)
        
        # Iterate through the remaining elements in the list
        for ele in nums[k:]:
            # If the new element is greater than or equal to the smallest element in the heap
            if ele >= self.heap[0]:
                # Remove the smallest element from the heap
                heapq.heappop(self.heap)
                # Add the new element to the heap
                heapq.heappush(self.heap, ele)
    
    def add(self, val: int) -> int:
        # If the heap size is less than k, add the new element to the heap
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        # If the new element is greater than or equal to the smallest element in the heap
        elif val >= self.heap[0]:
            # Remove the smallest element from the heap
            heapq.heappop(self.heap)
            # Add the new element to the heap
            heapq.heappush(self.heap, val)
        # Return the kth largest element (i.e., the smallest element in the heap)
        return self.heap[0]
```
The code utilizes the `heapq` library to create and manage the min-heap. The `__init__` method initializes the heap and adds the first k elements from the initial list. The `add` method handles new elements added to the stream, maintaining the heap size and ordering.

### Code
```python
import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap=[]
        self.k=k
        for ele in nums[:k]:
            heapq.heappush(self.heap,ele)
        
        for ele in nums[k:]:
            if ele>=self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap,ele)
            
    def add(self, val: int) -> int:
        if len(self.heap)<self.k:
            heapq.heappush(self.heap,val)
        elif val>=self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap,val)
        return self.heap[0]
```
### Complexity
- Time: O(log k) for the `add` method, as we perform a constant number of heap operations (push and pop). The `__init__` method has a time complexity of O(n log k) due to the initial iteration and heap insertion.
- Space: O(k) for storing the min-heap, as we maintain a maximum size of k elements.

## 🕵️‍♂️ Follow-up Questions (Optional)
1. How would you handle the case where the input stream is extremely large, and memory usage becomes a concern?
   - Answer: To reduce memory usage, we could consider using a more memory-efficient data structure, such as a balanced binary search tree, or implementing a streaming algorithm that doesn't require storing the entire stream.
2. Can you optimize the code further to improve performance?
   - Answer: The current implementation is already optimized, as it uses a min-heap to maintain the kth largest element in O(log k) time. However, micro-optimizations, such as using a custom heap implementation or reducing function call overhead, could provide minor performance improvements.

## Additional Analysis
### Core Intuition
The algorithmic strategy used is to maintain a min-heap of size k, ensuring the smallest element in the heap represents the kth largest element in the stream.

### Complexity Analysis
* Time complexity: O(log k) for the `add` method, O(n log k) for the `__init__` method
* Space complexity: O(k) for storing the min-heap
Justification:
+ Time complexity is dominated by the heap operations (push and pop), which have a logarithmic time complexity.
+ Space complexity is determined by the maximum size of the min-heap, which is k.

### Critical Optimizations
The current approach achieves optimal runtime and space boundaries, as it uses a min-heap to maintain the kth largest element in O(log k) time and O(k) space. However, minor micro-optimizations could be explored to further improve performance.