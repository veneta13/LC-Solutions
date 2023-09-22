class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1] * n

        before, after = 1, 1

        for i in range(1, n):
            res[i] = before * nums[i - 1]
            before *= nums[i - 1]

        for i in range(1, n + 1):
            res[n - i] *= after
            after *= nums[n - i]

        return res
