class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a=s.count("A")
        if(a<2 and "LLL" not in s):
            return True
        return False