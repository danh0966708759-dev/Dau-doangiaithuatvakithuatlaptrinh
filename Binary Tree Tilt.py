class Solution(object):
    def findTilt(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def t(r):
            if not r: return 0
            a, b = t(r.left), t(r.right)
            self.s += abs(a - b)
            return a + b + r.val
        self.s = 0
        t(root)
        return self.s