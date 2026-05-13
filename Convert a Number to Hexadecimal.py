class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num<0:
            num = (2**32) + num
        if num==0:
            return '0'
        hexchars = '0123456789abcdef'
        ans = ''
        while num>0:
            ans = hexchars[num%16] + ans
            num //= 16
        return ans