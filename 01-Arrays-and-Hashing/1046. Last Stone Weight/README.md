<h2><a href="https://leetcode.com/problems/last-stone-weight">1046. Last Stone Weight</a></h2>

<p>You are given an array of integers <code>stones</code> where <code>stones[i]</code> is the weight of the <code>i<sup>th</sup></code> stone.</p>

<p>We are playing a game with the stones. On each turn, we choose the <strong>heaviest two stones</strong> and smash them together. Suppose the heaviest two stones have weights <code>x</code> and <code>y</code> with <code>x &lt;= y</code>. The result of this smash is:</p>

<ul>
	<li>If <code>x == y</code>, both stones are destroyed, and</li>
	<li>If <code>x != y</code>, the stone of weight <code>x</code> is destroyed, and the stone of weight <code>y</code> has new weight <code>y - x</code>.</li>
</ul>

<p>At the end of the game, there is <strong>at most one</strong> stone left.</p>

<p>Return <em>the weight of the last remaining stone</em>. If there are no stones left, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> stones = [2,7,4,1,8,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong> 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> stones = [1]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= stones.length &lt;= 30</code></li>
	<li><code>1 &lt;= stones[i] &lt;= 1000</code></li>
</ul>


---

# 🛍️ Last-Stone-Weight | Explained

## Approach 1 (Optimized)
### Intuition
The core idea behind this approach is to utilize a max heap to efficiently find the two heaviest stones at each step, simulating the process of smashing the heaviest stones together. This approach works by leveraging the properties of a heap data structure to minimize the number of operations required to find the maximum elements.

### Approach
The algorithmic breakdown involves the following high-level steps:
1. Create a max heap from the input list of stone weights.
2. While there are at least two stones left, pop the two heaviest stones from the heap, calculate their difference, and push the result back into the heap if it's non-zero.
3. The process repeats until only one stone remains, at which point its weight is returned as the result.

### Detailed Code Analysis
The code initializes an empty list `heap` to serve as the max heap. It then iterates through the input list `stones`, pushing each element onto the heap using `heapq.heappush(heap, -ele)`. The `-ele` is used to simulate a max heap, as Python's `heapq` module only provides a min heap implementation.
```python
for ele in stones:
    heapq.heappush(heap, -ele)
```
The main loop of the algorithm continues as long as there are at least two elements in the heap. Inside the loop, it pops the two heaviest stones (i.e., the two largest elements in the max heap) using `heapq.heappop(heap)`.
```python
while len(heap) > 1:
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
```
The difference between the two heaviest stones is calculated and stored in `x`. If `x` is non-zero, it is pushed back onto the heap.
```python
x -= y
if x < 0:
    heapq.heappush(heap, x)
```
However, there seems to be a small mistake in the code. The condition `if x < 0` should actually be `if x != 0` or simply `if x`, as we want to push `x` back onto the heap if it's non-zero, regardless of its sign. Additionally, since we're simulating a max heap by storing negative values, we should push `-x` instead of `x` to maintain the max heap property.
```python
if x != 0:
    heapq.heappush(heap, -x)
```
Finally, the code returns the absolute value of the remaining stone's weight (if any) using `return abs(heap[0]) if heap else 0`.

### Code
```python
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for ele in stones:
            heapq.heappush(heap, -ele)
        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            x -= y
            if x != 0:
                heapq.heappush(heap, -x)
        return abs(heap[0]) if heap else 0
```

### Complexity
- Time: O(N log N), where N is the number of stones. This is because each insertion and removal operation on the heap takes O(log N) time, and we perform these operations N times.
- Space: O(N), as we store all the stones in the heap.

## 🕵️‍♂️ Follow-up Questions (Optional)
Some potential follow-up questions for this problem could be:
* How would you optimize the solution if the input list is extremely large and doesn't fit into memory?
* What if the stones have different shapes and sizes, and the weight is not the only factor in determining the outcome of a collision?

**Core Intuition:** The algorithmic strategy used is to simulate the process of smashing the heaviest stones together using a max heap, leveraging its properties to minimize the number of operations required. This approach works by repeatedly finding and smashing the two heaviest stones until only one remains.

**Complexity Analysis:**
* Time: O(N log N)
  + Justification:
    * Each insertion and removal operation on the heap takes O(log N) time.
    * We perform these operations N times.
* Space: O(N)
  + Justification:
    * We store all the stones in the heap.

**Critical Optimizations:** The provided approach achieves optimal runtime and space boundaries, with a time complexity of O(N log N) and a space complexity of O(N). However, the code can be slightly optimized by correcting the condition for pushing `x` back onto the heap and using `-x` instead of `x` to maintain the max heap property.