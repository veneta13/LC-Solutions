class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack_s = []
        stack_t = []

        for current in s:
            if current != '#':
                stack_s.append(current)
            elif stack_s:
                stack_s.pop()

        for current in t:
            if current != '#':
                stack_t.append(current)
            elif stack_t:
                stack_t.pop()

        return stack_s == stack_t
