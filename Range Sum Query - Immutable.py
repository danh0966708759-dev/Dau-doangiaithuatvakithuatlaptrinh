class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.preSum = [0]
        for i in range(len(nums)):
            self.preSum.append(nums[i] + self.preSum[i])        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.preSum[right+1] - self.preSum[left]