class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        st = set()
        while headA:
            st.add(headA)
            headA = headA.next
        while headB:
            if headB in st:
                return headB
            headB = headB.next
        return None