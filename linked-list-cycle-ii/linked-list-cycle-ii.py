# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def checkcycle(head):
            fast=head
            slow=head
            while fast and fast.next:
                fast=fast.next.next
                slow=slow.next
                if fast==slow:
                    return slow
            return None
        node= checkcycle(head)
        start=head
        if node is not None:
            while start is not node:
                start=start.next
                node=node.next
            return node
                      
        else:
            return None