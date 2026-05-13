class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
    def reverseList(self, head):
        prev=None; 
        while head: 
            head.next, prev, head = prev, head, head.next
        return prev       