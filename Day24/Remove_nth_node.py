# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node=ListNode(0,head)
        curr=node

        for i in range(n):
            head=head.next
        while head:
            curr=curr.next
            head=head.next
        curr.next=curr.next.next
        return node.next


    
        