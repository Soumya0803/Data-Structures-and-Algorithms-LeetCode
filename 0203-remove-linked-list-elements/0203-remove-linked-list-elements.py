# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0,head)
        prev,cur = dummy,head

        while cur:
            if cur.val == val:
                prev.next = prev.next.next
            else:
                prev = cur
            
            cur = cur.next
        return dummy.next
        
