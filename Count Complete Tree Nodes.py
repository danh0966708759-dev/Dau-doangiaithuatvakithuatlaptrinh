class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0

        left = root.left
        right = root.right
        l = 1
        r = 1
        while left:
            l += 1
            left = left.left
        while right:
            r += 1
            right = right.right
        print(left, right)
        if l == r:
            return 2 ** l - 1
        else:
            return self.countNodes(root.left) + 1 + self.countNodes(root.right)