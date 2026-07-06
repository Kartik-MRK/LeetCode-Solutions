1class Solution:
2    def isAlienSorted(self, words: List[str], order: str) -> bool:
3        alphabets={}
4        for i in range(len(order)):
5            alphabets[order[i]]=i
6        
7        for j in range(1,len(words)):
8            for i in range(len(max(words[j-1:j+1]))):
9                if len(words[j-1])==i:
10                    break
11                if len(words[j])==i:
12                    return False
13
14                if alphabets[words[j-1][i]]>alphabets[words[j][i]]:
15                    return False
16                    
17                if alphabets[words[j-1][i]]<alphabets[words[j][i]]:
18                    break
19        
20        return True
21
22
23        