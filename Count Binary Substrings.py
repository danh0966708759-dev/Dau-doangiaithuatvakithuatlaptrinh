class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev=0
        curr=1
        sums=0
        for i in range(1,len(s)):
            if(s[i]==s[i-1]):
                curr+=1
            else:
                sums+=min(prev,curr)
                prev=curr
                curr=1
        sums+=min(prev,curr)
        return sums 