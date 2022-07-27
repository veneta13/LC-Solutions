# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        answer_begin = ListNode(val=-101)
        answer = answer_begin

        while head is not None:
            if head.val != answer.val:
                answer.next = head
                answer = answer.next

            head = head.next

        answer.next = None
        return answer_begin.next
