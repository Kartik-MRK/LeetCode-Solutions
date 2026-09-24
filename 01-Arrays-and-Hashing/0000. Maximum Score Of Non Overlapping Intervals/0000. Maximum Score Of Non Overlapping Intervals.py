1from collections import deque
2class Solution:
3    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
4        def findnext(left,endpoint):
5            right=n-1
6            res=-1
7            while left<=right:
8                mid=(left+right)//2
9                if endpoint<intervals[mid][0]:
10                    res=mid
11                    right=mid-1
12                else:
13                    left=mid+1
14            return res
15        intervals=[row+[i] for i,row in enumerate(intervals)]
16        intervals.sort(key=lambda x:(x[0],x[1]))
17        n=len(intervals)
18        nextinterval=[-1]*n
19        for i in range(n-1):
20            nextinterval[i]=findnext(i+1,intervals[i][1])
21        dp={}
22        def maxscore(i, k):
23            if i == -1 or i >= n or k == 0:
24                return [0]
25
26            if (i, k) in dp:
27                return dp[(i, k)][:]
28
29            # Take current interval
30            take = maxscore(nextinterval[i], k - 1)[:]
31            take[0] += intervals[i][2]
32            take.append(intervals[i][3])
33
34            # Skip current interval
35            skip = maxscore(i + 1, k)[:]
36
37            if take[0] > skip[0]:
38                dp[(i, k)] = take[:]
39
40            elif take[0] < skip[0]:
41                dp[(i, k)] = skip[:]
42
43            else:
44                # Compare only the index lists when scores tie
45                take_indices = sorted(take[1:])
46                skip_indices = sorted(skip[1:])
47
48                if take_indices < skip_indices:
49                    dp[(i, k)] = [take[0]] + take_indices
50                else:
51                    dp[(i, k)] = [skip[0]] + skip_indices
52
53            return dp[(i, k)][:]
54
55            
56            
57        
58        return sorted(maxscore(0,4)[1:])
59
60
61
62        