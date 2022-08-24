class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """

        if target < letters[0] or target >= letters[-1]:
            return letters[0]

        left = 0
        right = len(letters) - 1

        while left <= right:
            current = (left + right) // 2

            if target < letters[current]:
                right = current - 1
            else:
                left = current + 1

        return letters[left]
