class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = Counter(s)
        
        odd = False
        res = 0
        
        for k,v in freq.items():
            if v % 2 == 0:
                res += v
            else:
                res += v-1
                odd = True
        
        if odd:
            res += 1
            
        return res