class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum=0
        s=0
        for i in range(len(nums)):
            if nums[i] /1 >=10:
                sum+=nums[i]
            else:
                s+=nums[i]
        if sum == s:
            return False
        else:
            return True