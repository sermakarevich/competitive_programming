# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def traverse_list_node(self, l):
        vals = [l.val]
        while l.next:
            l = l.next
            vals.append(l.val)
        return vals

    def reverse_and_join_vals(self, vals):
        reversed_vals = vals[::-1]
        val = int(''.join([str(i) for i in reversed_vals]))
        return val

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_vals = self.traverse_list_node(l1)
        l2_vals = self.traverse_list_node(l2)

        l1_val = self.reverse_and_join_vals(l1_vals)
        l2_val = self.reverse_and_join_vals(l2_vals)
        l_val = l1_val + l2_val
        reversed_l_val = str(l_val)[::-1]
        print(reversed_l_val)
        l_nodes = [ListNode(val=val) for val in reversed_l_val]
        for index in range(1, len(l_nodes)):
            l_nodes[index - 1].next = l_nodes[index]
        return l_nodes[0]

l1 = ListNode(val = 1)
l1.next = ListNode(val = 8)
l2 = ListNode(val=0)
s = Solution()
print(s.addTwoNumbers(l1, l2))