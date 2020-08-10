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


def kth_to_last(k, ll):
    for _ in range(1, k):
        if ll.head.next is not None:
            ll.head = ll.head.next
        else:
            return
    return ll


nodes_ = [random.randint(0, 10) for i in range(10)]
k = 5
print(nodes_)
ll = LinkedList(nodes=nodes_)
print(ll)
ll = kth_to_last(k, ll)
print(ll)