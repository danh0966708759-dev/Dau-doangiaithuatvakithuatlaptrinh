class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        match = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for ch in s:
            if ch in match.values():      
                stack.append(ch)
            else:                         
                if not stack or stack.pop() != match[ch]:
                    return False
        
        return not stack