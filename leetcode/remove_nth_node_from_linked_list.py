class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        nodes = []
        while self.next:
            nodes.append(str(self.val))
            self = self.next
        nodes.append(str(self.val))
        return " -> ".join(nodes)


class ListNodes:
    def __init__(self, node_values):
        self.head = ListNode(val=node_values[0])
        node = ListNode(val=node_values[1])
        self.head.next = node
        for node_val in node_values[2:]:
            node_ = ListNode(val=node_val)
            node.next = node_
            node = node.next

    def __repr__(self):
        nodes = []
        head = self.head
        while head.next:
            nodes.append(str(head.val))
            head = head.next
        nodes.append(str(head.val))
        return " -> ".join(nodes)


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first = last = head
        for i in range(n):
            last = last.next
            print('last', end=': ')
            print(last)
        if not last:
            return head.next

        while last.next:
            print('first', end=': ')
            first = first.next
            print(first)
            print('last', end=': ')
            last = last.next
            print(last)
            print('head', end=': ')
            print(head)
        first.next = first.next.next
        print('first', end=': ')
        print(first)
        return head


nodes = [1, 2, 3, 5]
list_nodes = ListNodes(node_values=nodes)
print(list_nodes)

s = Solution()
h = s.removeNthFromEnd(list_nodes.head, n=4)
print(h)