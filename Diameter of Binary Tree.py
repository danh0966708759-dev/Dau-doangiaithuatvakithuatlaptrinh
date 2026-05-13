class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        result = [0]
        def depth(root):
            if not root:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            result[0] = max(result[0], left + right)
            return 1 + max(left, right)
        depth(root)
        return result[0]