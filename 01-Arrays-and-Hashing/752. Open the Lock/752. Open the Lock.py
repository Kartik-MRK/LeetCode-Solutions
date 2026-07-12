1from collections import deque
2class Solution:
3    def openLock(self, deadends: List[str], target: str) -> int:
4        dead=set(deadends)
5        if 0000 in dead:
6            return -1
7        visited=set()
8        queue=deque([[0000,0]])
9        visited.add(0000)
10        while queue:
11            curr,turn=queue.popleft()
12            if curr==target:
13                return turn
14            for i in range(4):
15                ele=list(curr)
16                ele[i]=(int(ele[i])+1)%10
17                ele[i]=str(ele[i])
18                nxt=.join(ele)
19                if  nxt not in dead and nxt not in visited:
20                    visited.add(nxt)
21                    queue.append([nxt,turn+1])
22
23                ele=list(curr)
24                ele[i]=(int(ele[i])-1)%10
25                ele[i]=str(ele[i])
26                prev=.join(ele)
27                if  prev not in dead and prev not in visited:
28                    visited.add(prev)
29                    queue.append([prev,turn+1])
30        
31        return -1
32
33
34                
35
36                
37
38
39
40
41        