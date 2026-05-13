class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = ""
        count = 0
        for i in range(0,len(s), k):
            val = s[i:i+k]
            if count%2 == 0:
                val = val[::-1]
            result+=val
            count+=1

        return result