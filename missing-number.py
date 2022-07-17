class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = [False for i in range(len(nums) + 1)]

        for num in nums:
            seen[num] = True

        for i in range(len(nums) + 1):
            if not seen[i]:
                return i
