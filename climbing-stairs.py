class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dyn = [1, 1]

        for i in range(2, n + 1):
            dyn.append(dyn[i - 1] + dyn[i - 2])

        return dyn[n]
