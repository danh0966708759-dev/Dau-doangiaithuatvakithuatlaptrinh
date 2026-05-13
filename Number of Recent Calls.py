class RecentCounter(object):

    def __init__(self):
        self.result=deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.result.append(t)
        k=t-3000
    
        while self.result and self.result[0]<k:
            self.result.popleft()
        
        return len(self.result)