class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        stack=[]
        res=[]
        while stack or root:
            if root:
                stack.append(root)
                res.append(root.val)
                root=root.left
            else:
                root=stack.pop()
                root=root.right
        return res