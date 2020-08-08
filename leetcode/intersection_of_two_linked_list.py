class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        [1,2,3]
        [5,6,7, 8, 2]
        """
        if not headA or not headB:
            return None
        nodesA = set()
        nodesB = set()
        while headA and headB:
            if headA in nodesB:
                return headA
            nodesA.add(headA)
            headA = headA.next
            if headB in nodesA:
                return headB
            nodesB.add(headB)
            headB = headB.next
        while headA:
            if headA in nodesB:
                return headA
            nodesA.add(headA)
            headA = headA.next
        while headB:
            if headB in nodesA:
                return headB
            headB = headB.next
        return None