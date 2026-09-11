1class Solution:
2    def totalNumbers(self, digits: List[int]) -> int:
3        n=len(digits)
4        seen=set()
5        for i in range(len(digits)):
6            if digits[i]==0:
7                continue
8            for j in range(n):
9                if i==j:
10                    continue
11                for k in range(n):
12                    if k==i or k==j:
13                        continue
14                    digit=digits[i]*100+digits[j]*10+digits[k]
15                    if digit not in seen and digit%2==0:
16                        seen.add(digit)
17                    
18                
19            
20        return len(seen)
21
22        