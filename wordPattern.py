class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        pattern=list(pattern)
        s=s.split()
        if len(pattern)!=len(s):
            return False
        a=zip(pattern,s)
        b=[]
        for i in a:
            b.append(i)
        return len(set(b))==len(set(pattern)) and len(set(b))==len(set(s))
                    