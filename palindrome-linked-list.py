# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        input_list = []

        while head is not None:
            input_list.append(head.val)
            head = head.next

        reverse_list = input_list[:]
        reverse_list.reverse()

        return input_list == reverse_list
