import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join([str(i) for i in nodes])


def remove_duplicates(ll):
    head = ll.head
    seen_nodes = set([head.data])
    while head.next:
        if head.next.data in seen_nodes:
            head.next = head.next.next
        else:
            seen_nodes.add(head.next.data)
            head = head.next
    return ll


nodes_ = [random.randint(0, 10) for i in range(10)]
print(nodes_)
ll = LinkedList(nodes=nodes_)
print(ll)
ll = remove_duplicates(ll)
print(ll)

