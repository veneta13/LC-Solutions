class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        counterS = {}
        counterT = {}

        for idx in range(len(t)):
            counterS[s[idx]] = 1 + (counterS[s[idx]] if s[idx] in counterS else 0)
            counterT[t[idx]] = 1 + (counterT[t[idx]] if t[idx] in counterT else 0)

        return counterS == counterT
