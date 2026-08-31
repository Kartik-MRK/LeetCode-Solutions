1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
8        prev=head
9        curr=head.next
10        i=1
11        distance=[]
12        if not prev:
13            return [-1,-1]
14        while curr and curr.next:
15            if prev.val>curr.val and curr.next.val>curr.val:
16                distance.append(i)
17            elif prev.val<curr.val and curr.next.val<curr.val:
18                distance.append(i)
19            prev=curr
20            curr=curr.next
21            i+=1
22        if len(distance)<2:
23            return [-1,-1]
24        maxdist=distance[-1]-distance[0]
25        mindist=float(inf)
26        for i in range(1,len(distance)):
27            mindist=min(mindist,distance[i]-distance[i-1])
28        return [mindist,maxdist]
29
30        
31        