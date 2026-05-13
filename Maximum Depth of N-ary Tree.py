class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        stack = []
        if root:
            stack += [(root,1)]
        maxDepth = 0
        while stack:
            node,depth = stack.pop()
            maxDepth = max(maxDepth, depth)
            for child in node.children:
                stack += (child,depth+1),
        return maxDepth