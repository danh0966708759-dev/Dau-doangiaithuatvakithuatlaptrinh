class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        s=[root]
        r=[]
        while s:
            n=s.pop()
            if n.left:
                s.append(n.left)
            if n.right:
                s.append(n.right)
            r.append(n.val)
        return r[::-1]