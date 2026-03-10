class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def bst(nums):
            if nums == []:
                return None
            n = len(nums)
            root = TreeNode(nums[n//2])
            root.left = bst(nums[:n//2])
            root.right = bst(nums[n//2+1:])
            return root
        
        return bst(nums)