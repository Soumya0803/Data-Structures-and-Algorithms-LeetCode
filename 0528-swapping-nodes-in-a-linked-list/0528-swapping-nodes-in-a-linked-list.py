# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        left = head
        for _ in range(k - 1):
            left = left.next

        temp  = left
        right = head
        while temp.next:
            right = right.next
            temp = temp.next

        left.val, right.val = right.val, left.val
        return head