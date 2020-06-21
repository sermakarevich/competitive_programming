class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    #     if nodes is not None:
    #         val = nodes.pop()
    #         self.next = ListNode(vals=val)

    def __repr__(self):
        node = self
        vals = []
        while node:
            vals.append(str(node.val))
            node = node.next
        return '->'.join(vals)


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l2:
            return l1
        if not l1:
            return l2
        vals = []
        while l1 and l2:
            if l1.val <= l2.val:
                vals.append(l1.val)
                l1 = l1.next
            else:
                vals.append(l2.val)
                l2 = l2.next
        while l1:
            val = l1.val
            vals.append(val)
            l1 = l1.next
        while l2:
            val = l2.val
            vals.append(val)
            l2 = l2.next
        nodes = [ListNode(val=val) for val in vals]
        for ind in range(1, len(nodes)):
            nodes[ind-1].next = nodes[ind]
        return nodes[0]


ln = ListNode(val=1)
second = ListNode(val=2)
ln.next = second
second.next = ListNode(val=4)
print(ln)

ln2 = ListNode(val=0)
second2 = ListNode(val=3)
ln2.next = second2
second2.next = ListNode(val=5)
print(ln2)

s = Solution()
merged = s.mergeTwoLists(ln, ln2)
print(merged)