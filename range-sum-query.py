class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        current_sum = 0

        for i in range(left, right + 1):
            current_sum += self.nums[i]

        return current_sum
