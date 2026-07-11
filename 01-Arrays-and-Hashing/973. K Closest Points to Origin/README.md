<h2><a href="https://leetcode.com/problems/k-closest-points-to-origin">973. K Closest Points to Origin</a></h2>

<p>Given an array of <code>points</code> where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> represents a point on the <strong>X-Y</strong> plane and an integer <code>k</code>, return the <code>k</code> closest points to the origin <code>(0, 0)</code>.</p>

<p>The distance between two points on the <strong>X-Y</strong> plane is the Euclidean distance (i.e., <code>√(x<sub>1</sub> - x<sub>2</sub>)<sup>2</sup> + (y<sub>1</sub> - y<sub>2</sub>)<sup>2</sup></code>).</p>

<p>You may return the answer in <strong>any order</strong>. The answer is <strong>guaranteed</strong> to be <strong>unique</strong> (except for the order that it is in).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/03/closestplane1.jpg" style="width: 400px; height: 400px;">
<pre><strong>Input:</strong> points = [[1,3],[-2,2]], k = 1
<strong>Output:</strong> [[-2,2]]
<strong>Explanation:</strong>
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) &lt; sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> points = [[3,3],[5,-1],[-2,4]], k = 2
<strong>Output:</strong> [[3,3],[-2,4]]
<strong>Explanation:</strong> The answer [[-2,4],[3,3]] would also be accepted.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= points.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
</ul>


---

# 🛍️ K-Closest-Points-to-Origin | Explained

## Approach 1 (Heap-Based)
### Intuition
The core idea behind this approach is to utilize a heap data structure to efficiently find the k closest points to the origin. This works by maintaining a min-heap of the k closest points encountered so far, where the point with the maximum distance (i.e., the "worst" point in the heap) is always at the top and can be easily replaced if a closer point is found.
### Approach
1. Initialize an empty min-heap.
2. Iterate through each point in the input list.
3. For each point, calculate its distance from the origin (using the Euclidean distance formula).
4. If the heap is not full (i.e., it has less than k points), push the point onto the heap.
5. If the heap is full and the current point is closer to the origin than the "worst" point in the heap, remove the worst point from the heap and push the current point onto the heap.
6. After iterating through all points, the heap will contain the k closest points to the origin.

### Detailed Code Analysis
The code starts by importing the necessary modules, `math` and `heapq`. The `Solution` class has a method `kClosest` that takes a list of points and an integer `k` as input.

- Line 5: `heap=[]` - Initializes an empty list to be used as a min-heap.
- Line 7-17: Iterates through each point in the input list. For each point:
  - Line 9: `dorigin=-sqrt(x**2+y**2)` - Calculates the negative Euclidean distance of the point from the origin. The negative sign is used because Python's `heapq` module only provides a min-heap implementation, but we want the point with the maximum distance (i.e., the "worst" point) to be at the top of the heap.
  - Line 10-11: If the heap is not full, pushes the point onto the heap.
  - Line 13-16: If the heap is full and the current point is closer to the origin than the worst point in the heap, removes the worst point from the heap and pushes the current point onto the heap.
- Line 18-19: After iterating through all points, extracts the points from the heap and returns them as the result.

### Code
```python
import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        res=[]
        for x,y in points:
            dorigin=-math.sqrt(x**2+y**2)
            if len(heap)<k:
                heapq.heappush(heap,(dorigin,[x,y]))
            else:
                if heap[0][0]<=dorigin:
                    dele=heapq.heappop(heap)
                    heapq.heappush(heap,(dorigin,[x,y]))
        for key,value in heap:
            res.append(value)
        return res
```

### Complexity
- Time: O(N log k) - where N is the number of points. This is because we iterate through all points (O(N)) and for each point, we perform a heap operation (O(log k)).
- Space: O(k) - where k is the number of closest points to find. This is because we store the k closest points in the heap.

## 🕵️‍♂️ Follow-up Questions (Optional)
Some possible follow-up questions for this problem include:
- How would you handle the case where two or more points have the same distance from the origin?
- What if the input points are not in a list, but are instead generated on the fly by a separate process?

# 🔍 Detailed Analysis
## Core Intuition
The algorithmic strategy used here is to leverage a heap data structure to maintain a sorted collection of the k closest points to the origin, with the point having the maximum distance always at the top and easily replaceable.
## Complexity Analysis
- Time: **O(N log k)** 
  * The reason for this time complexity is that we perform a heap operation for each of the N points, and each heap operation takes O(log k) time.
- Space: **O(k)**
  * The reason for this space complexity is that we store the k closest points in the heap.
## Critical Optimizations
The current approach achieves optimal runtime boundaries, but one potential micro-optimization could be to use a more efficient method for calculating the Euclidean distance, such as using the `math.hypot` function instead of `math.sqrt` and `x**2 + y**2`. However, this would likely have a negligible impact on performance.