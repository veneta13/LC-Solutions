# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        mid = head
        counter = 1
        current = 1

        while head is not None:
            if counter / current == 2:
                mid = mid.next
                current += 1
            counter += 1
            head = head.next

        return mid
