1class Solution:
2    def smallestPalindrome(self, s: str) -> str:
3        k=.join(sorted(s))
4        n=len(s)
5        arr=['_']*n
6        index=0
7        fill=0
8        
9        while index<n-1:
10            if k[index]!=k[index+1]:
11                arr[n//2]=k[index]
12                index+=1
13            else:
14                arr[fill]=arr[n-fill-1]=k[index]
15                index+=2
16                fill+=1 
17        if arr[n//2]=='_':
18            arr[n//2]=k[n-1]
19        
20        return .join(arr)
21            
22
23        