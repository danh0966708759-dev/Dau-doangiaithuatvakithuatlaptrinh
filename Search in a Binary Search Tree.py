class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        def iterative_tree_search(root, val):
            while root is not None and val != root.val:
                if val < root.val:
                    root = root.left
                else:
                    root = root.right
            return root
        return iterative_tree_search(root, val)