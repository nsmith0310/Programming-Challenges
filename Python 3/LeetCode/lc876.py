# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        l = []
        
        while head!=None:
            l.append(head)
            head = head.next
        
        
        return (l[len(l)//2])
        
