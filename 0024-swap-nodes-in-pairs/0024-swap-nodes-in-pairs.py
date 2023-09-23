# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):   
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
            
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            # save ptrs
            nextPair = curr.next.next
            second = curr.next

            # reverse this pair
            second.next = curr
            curr.next = nextPair
            prev.next = second

            # update ptrs
            prev = curr
            curr = nextPair

        return dummy.next