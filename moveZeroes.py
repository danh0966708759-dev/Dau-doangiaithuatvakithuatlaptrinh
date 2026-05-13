class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nonZero = 0
        if n != 1:
            for i in range(n):
                if nums[i]!=0:
                    nums[i],nums[nonZero] = nums[nonZero],nums[i]
                    nonZero+=1 