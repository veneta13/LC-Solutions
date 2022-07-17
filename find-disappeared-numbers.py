class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        missing = [True for i in range(len(nums) + 1)]
        answer = []

        for num in nums:
            missing[num] = False

        for i in range(1, len(nums) + 1):
            if missing[i]:
                answer.append(i)

        return answer
