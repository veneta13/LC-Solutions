class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        anagramMap = {}

        for curr_str in strs:
            count = [0] * 26

            for curr_lett in curr_str:
                count[ord(curr_lett) - ord("a")] += 1

            const_count = tuple(count)

            if const_count in anagramMap:
                anagramMap[const_count].append(curr_str)
            else:
                anagramMap[const_count] = [curr_str]

        return anagramMap.values()
