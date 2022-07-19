class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = -100000
        current_sum = 0

        for num in nums:
            current_sum += num
            answer = current_sum if answer < current_sum else answer
            current_sum = current_sum if current_sum > 0 else 0

        return answer
