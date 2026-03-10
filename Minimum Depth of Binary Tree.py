class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def height(temp):
            if not temp:
                return 0
            ldepth = height(temp.left)
            rdepth = height(temp.right)
            if not temp.left and not temp.right:
                return 1
            if not temp.left:
                return 1+rdepth
            if not temp.right:
                return 1+ldepth
            return 1+min(ldepth,rdepth)
        return height(root)