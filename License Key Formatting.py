class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ans, j, count = '', len(s)-1, 0
        while j>=0:
            if s[j] != '-':
                if count == k:
                    count = 0
                    ans = '-' + ans
                if count <= k:
                    ans = s[j].upper() + ans
                    count+=1
            j-=1
        return ans  