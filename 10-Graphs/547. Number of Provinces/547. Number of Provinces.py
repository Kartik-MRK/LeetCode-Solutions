1class Solution:
2    def findCircleNum(self, isConnected: List[List[int]]) -> int:
3        n=len(isConnected)
4        ans=n
5        parent=[i for i in range(n)]
6        size=[1]*n
7
8        def find(a):
9            if parent[a]==a:
10                return a
11            parent[a]=find(parent[a])
12            return parent[a]
13        
14        for i in range(n):
15            for j in range(n):
16                if i==j or i>j:
17                    continue
18
19                if isConnected[i][j]:
20                    x=find(i)
21                    y=find(j)
22
23                    if x!=y:
24                        ans-=1
25                    else:
26                        continue
27                    
28                    if size[x]>size[y]:
29                        parent[y]=x
30                        size[x]+=size[y]
31                        
32                    elif size[y]>size[x]:
33                        parent[x]=y
34                        size[y]+=size[x]
35
36                    else:
37                        parent[y]=x
38                        size[x]+=size[y]
39
40        return ans    
41        