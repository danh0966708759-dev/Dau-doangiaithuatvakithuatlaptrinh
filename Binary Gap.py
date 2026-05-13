class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        b=bin(n)[2:]
        r=0
        last=-1
        for i in range(len(b)):
            if b[i]=="1":
                if last!=-1:
                    r=max(r,i-last)
                last=i
        return r