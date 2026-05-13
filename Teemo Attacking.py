class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        total = 0
        next_time = 0
        for time in timeSeries:
            if time>next_time:
                total += duration 
            else:
                total += duration - (next_time - time)
            next_time = time + duration
        return total 