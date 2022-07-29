class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = map(lambda x: x * x, nums)
        return sorted(answer)
