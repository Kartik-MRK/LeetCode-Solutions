1class Solution:
2    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
3        visited=[False]*numCourses
4        graph={i:[] for i in range(numCourses)}
5        for course,pre in prerequisites:
6            graph[course].append(pre)
7        
8
9        def dfs(course):
10            if visited[course]:
11                return False
12            if not graph[course]:
13                return True
14            visited[course]=True
15            for ele in graph[course]:
16                if not dfs(ele):
17                    return False
18            graph[course]=[]
19            visited[course]=False
20            
21            return True
22                
23        for i in range(numCourses):
24            if not dfs(i):
25                return False
26        return True
27
28
29        
30
31
32        