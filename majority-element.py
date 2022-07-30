class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0

        for current in nums:
            if counter == 0:
                answer = current

            counter = counter + 1 if answer == current else counter - 1

        return answer
