<h2><a href="https://leetcode.com/problems/course-schedule">207. Course Schedule</a></h2>

<p>There are a total of <code>numCourses</code> courses you have to take, labeled from <code>0</code> to <code>numCourses - 1</code>. You are given an array <code>prerequisites</code> where <code>prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that you <strong>must</strong> take course <code>b<sub>i</sub></code> first if you want to take course <code>a<sub>i</sub></code>.</p>

<ul>
	<li>For example, the pair <code>[0, 1]</code>, indicates that to take course <code>0</code> you have to first take course <code>1</code>.</li>
</ul>

<p>Return <code>true</code> if you can finish all courses. Otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> numCourses = 2, prerequisites = [[1,0]]
<strong>Output:</strong> true
<strong>Explanation:</strong> There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> numCourses = 2, prerequisites = [[1,0],[0,1]]
<strong>Output:</strong> false
<strong>Explanation:</strong> There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= numCourses &lt;= 2000</code></li>
	<li><code>0 &lt;= prerequisites.length &lt;= 5000</code></li>
	<li><code>prerequisites[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; numCourses</code></li>
	<li>All the pairs prerequisites[i] are <strong>unique</strong>.</li>
</ul>


---

# 🛍️ Course-Schedule | Explained

## Approach 1 (Optimized Depth-First Search)
### Intuition
The provided code solution utilizes a Depth-First Search (DFS) approach to detect cycles in the course prerequisite graph, leveraging the idea that a course can be finished only if all its prerequisites can be finished. This approach works by exploring the prerequisites of each course and ensuring that there are no circular dependencies.
### Approach
The high-level logic flow of this approach is as follows:
1. Create a graph data structure to store the courses and their prerequisites.
2. Initialize a visited array to keep track of the courses that are currently being visited.
3. Perform DFS on each unvisited course to check if it can be finished.
4. During the DFS, mark the current course as visited and recursively visit its prerequisites.
5. If a course is revisited during the DFS, it indicates a cycle, and the function returns False.
6. If the DFS completes without finding a cycle, the function returns True.

### Detailed Code Analysis
Let's dive into the code block line-by-line:
- Lines 1-2: The `canFinish` function is defined, taking the number of courses and the prerequisites as input.
- Line 3: The `visited` array is initialized with `False` values, representing the courses that are not currently being visited.
- Line 4: The `graph` dictionary is created to store the courses and their prerequisites.
- Lines 5-6: The prerequisites are added to the `graph` dictionary.
- Lines 9-21: The `dfs` function is defined to perform the Depth-First Search on a given course.
- Line 10: If the course is already visited, it indicates a cycle, and the function returns `False`.
- Line 12: If the course has no prerequisites, it can be finished, and the function returns `True`.
- Lines 14-20: The course is marked as visited, and its prerequisites are recursively visited.
- Line 19: After visiting all prerequisites, the course is marked as unvisited to allow other courses to visit it.
- Lines 23-26: The `dfs` function is called on each unvisited course to check if it can be finished.

### Code
```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited=[False]*numCourses
        graph={i:[] for i in range(numCourses)}
        for course,pre in prerequisites:
            graph[course].append(pre)
        
        def dfs(course):
            if visited[course]:
                return False
            if not graph[course]:
                return True
            visited[course]=True
            for ele in graph[course]:
                if not dfs(ele):
                    return False
            graph[course]=[]
            visited[course]=False
            
            return True
                
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
```

### Complexity
- Time: O(N + M), where N is the number of courses and M is the number of prerequisites. This is because each course and prerequisite is visited once during the DFS.
- Space: O(N + M), where N is the number of courses and M is the number of prerequisites. This is because the `graph` dictionary and the `visited` array require O(N + M) space.

## 🕵️‍♂️ Follow-up Questions (Optional)
Some common follow-up questions for this problem include:
- How would you optimize the solution for very large inputs?
- What are some potential edge cases that the solution should handle?

To address these questions, the provided solution already achieves optimal runtime and space boundaries, with a time complexity of O(N + M) and a space complexity of O(N + M). However, to further optimize the solution, you could consider using a more efficient data structure, such as an adjacency list representation of the graph, or using a more advanced algorithm, such as Tarjan's strongly connected components algorithm.

Core Intuition: The algorithmic strategy used is a Depth-First Search (DFS) approach to detect cycles in the course prerequisite graph. The solution works by exploring the prerequisites of each course and ensuring that there are no circular dependencies.
Complexity Analysis:
* Time: O(N + M)
	+ The solution visits each course and prerequisite once during the DFS.
* Space: O(N + M)
	+ The `graph` dictionary and the `visited` array require O(N + M) space.
Critical Optimizations: The provided solution achieves optimal runtime and space boundaries. However, minor optimizations, such as using a more efficient data structure or algorithm, could potentially improve the solution's performance.