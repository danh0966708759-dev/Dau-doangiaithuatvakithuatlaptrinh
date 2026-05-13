class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        f = flowerbed
        for i in range(len(f)):
            leftOk = i == 0 or f[i-1] == 0
            rightOk = i == len(f) -1 or f[i+1] == 0
            if leftOk and f[i] == 0 and rightOk:
                f[i] = 1
                n -= 1
        return n <= 0