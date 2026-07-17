1import heapq
2class FreqStack:
3
4    def __init__(self):
5        self.freq={}
6        self.bucket={}
7        self.maxfreq=0
8        
9
10    def push(self, val: int) -> None:
11        self.freq[val]=self.freq.get(val,0)+1
12        self.maxfreq=max(self.freq[val],self.maxfreq)
13        if self.freq[val] not in self.bucket:
14            self.bucket[self.freq[val]]=[]
15        self.bucket[self.freq[val]].append(val)
16
17    def pop(self) -> int:
18        popval=self.bucket[self.maxfreq].pop()
19        self.freq[popval]=self.freq.get(popval,0)-1
20        if self.bucket[self.maxfreq]==[]:
21            self.maxfreq-=1
22        return popval
23                
24        
25
26
27# Your FreqStack object will be instantiated and called as such:
28# obj = FreqStack()
29# obj.push(val)
30# param_2 = obj.pop()