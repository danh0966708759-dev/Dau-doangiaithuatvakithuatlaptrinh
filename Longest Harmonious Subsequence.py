class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        count = Counter(nums)
        ans = 0
        for key in count:
            if key + 1 in count:
                ans = max(ans, count[key] + count[key + 1])
        return ans