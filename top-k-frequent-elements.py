class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = {}

        for current in nums:
            counter[current] = counter.get(current, 0) + 1

        sorted_freq = sorted(counter.items(), key=lambda x: x[1], reverse=True)[:k]

        return [item[0] for item in sorted_freq]
