1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        prev=None
9        temp=head
10        while temp:
11            tmp=temp.next
12            temp.next=prev
13            prev=temp
14            temp=tmp
15
16        return prev
17        