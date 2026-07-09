<h2><a href="https://leetcode.com/problems/number-of-provinces">547. Number of Provinces</a></h2>

<p>There are <code>n</code> cities. Some of them are connected, while some are not. If city <code>a</code> is connected directly with city <code>b</code>, and city <code>b</code> is connected directly with city <code>c</code>, then city <code>a</code> is connected indirectly with city <code>c</code>.</p>

<p>A <strong>province</strong> is a group of directly or indirectly connected cities and no other cities outside of the group.</p>

<p>You are given an <code>n x n</code> matrix <code>isConnected</code> where <code>isConnected[i][j] = 1</code> if the <code>i<sup>th</sup></code> city and the <code>j<sup>th</sup></code> city are directly connected, and <code>isConnected[i][j] = 0</code> otherwise.</p>

<p>Return <em>the total number of <strong>provinces</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/24/graph1.jpg" style="width: 222px; height: 142px;">
<pre><strong>Input:</strong> isConnected = [[1,1,0],[1,1,0],[0,0,1]]
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/24/graph2.jpg" style="width: 222px; height: 142px;">
<pre><strong>Input:</strong> isConnected = [[1,0,0],[0,1,0],[0,0,1]]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 200</code></li>
	<li><code>n == isConnected.length</code></li>
	<li><code>n == isConnected[i].length</code></li>
	<li><code>isConnected[i][j]</code> is <code>1</code> or <code>0</code>.</li>
	<li><code>isConnected[i][i] == 1</code></li>
	<li><code>isConnected[i][j] == isConnected[j][i]</code></li>
</ul>


---

# 🛍️ Number-of-Provinces | Explained

## Approach 1 (e.g., Union-Find)
### Intuition
The core idea behind this approach is to use a union-find data structure to group connected provinces together. This works because two provinces are in the same group if and only if there is a path between them, either directly or indirectly. By counting the number of distinct groups, we can determine the number of provinces.

### Approach
The algorithm works by iterating over each pair of provinces. If two provinces are connected and belong to different groups, we merge their groups by updating the parent of one group to point to the other group. This process continues until all pairs of provinces have been checked.

### Detailed Code Analysis
The code initializes several key variables:
- `n`: the total number of provinces.
- `ans`: the initial count of provinces, which will be decremented as groups are merged.
- `parent`: an array to store the parent of each province.
- `size`: an array to store the size of each group.

The `find(a)` function is a recursive function that finds the root of the group containing province `a`. It uses path compression to optimize the search by updating the parent of each province to point directly to the root as it searches.

The main loop iterates over each pair of provinces. If two provinces are connected (`isConnected[i][j]` is `True`) and belong to different groups (`x != y`), the code merges their groups by updating the parent of one group to point to the other group. The `size` array is updated accordingly to reflect the new group size.

### Code
```python
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        ans = n
        parent = [i for i in range(n)]
        size = [1] * n

        def find(a):
            if parent[a] == a:
                return a
            parent[a] = find(parent[a])
            return parent[a]

        for i in range(n):
            for j in range(n):
                if i == j or i > j:
                    continue

                if isConnected[i][j]:
                    x = find(i)
                    y = find(j)

                    if x != y:
                        ans -= 1
                    else:
                        continue

                    if size[x] > size[y]:
                        parent[y] = x
                        size[x] += size[y]

                    elif size[y] > size[x]:
                        parent[x] = y
                        size[y] += size[x]

                    else:
                        parent[y] = x
                        size[x] += size[y]

        return ans
```

### Complexity
- Time: O(n^2 * α(n)), where α(n) is the inverse Ackermann function, which grows very slowly. In practice, the time complexity can be considered as O(n^2) because α(n) is typically very small.
- Space: O(n), where n is the number of provinces. The space is used to store the parent and size arrays.

## 🕵️‍♂️ Follow-up Questions (Optional)
Some potential follow-up questions could be:
- How would you optimize the solution if the input graph is sparse?
- How would you handle the case where the input graph is very large and cannot fit into memory?

**Core Intuition**: This solution uses a union-find data structure to efficiently group connected provinces together, allowing it to count the number of distinct groups. The union-find approach enables the algorithm to avoid explicit graph traversal and instead focus on merging groups as it iterates over province connections.

**Complexity Analysis**:
* Time: O(n^2 * α(n))
* Space: O(n)
Justification:
- Time complexity is dominated by the nested loop over all pairs of provinces, resulting in a quadratic term. The inverse Ackermann function α(n) represents the overhead of the union-find operations.
- Space complexity is linear because we need to store the parent and size arrays for each province.

**Critical Optimizations**: This approach achieves optimal runtime boundaries for the given problem. The use of path compression in the union-find data structure minimizes the overhead of find operations, and the size array helps to ensure that smaller groups are always merged into larger ones, reducing the number of recursive find calls. No further microscopic micro-optimizations are necessary for this solution.