class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x ^ y
        ans = 0
        while z > 0:
            ans += z % 2
            z >>= 1
        return ans