class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        mn=min(nums)
        mx=max(nums)
        for i in nums:
            if mn<i<mx:
                ans+=1

        return ans