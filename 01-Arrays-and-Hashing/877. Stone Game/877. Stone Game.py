1class Solution:
2    def stoneGame(self, piles: List[int]) -> bool:
3        dp={}
4        def dfs(l,r):
5            if l>r:
6                return 0
7            if (l,r) in dp:
8                return dp[(l,r)]
9            even=True if (r-l+1)%2==0 else False
10            left=piles[l] if even else 0
11            right=piles[r] if even else 0
12            dp[(l,r)]=max(dfs(l+1,r)+left,dfs(l,r-1)+right)
13            return dp[(l,r)]
14        
15        return dfs(0,len(piles)-1)>sum(piles)//2
16
17
18        