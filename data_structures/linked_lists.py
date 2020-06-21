from collections import deque

llist = deque("abcde")
print(llist)

# Both append() and pop() add or remove elements from the right side of the linked list.
llist.append("f")
print(llist)

print(llist.pop())
print(llist)

# However, you can also use deque to quickly add or remove elements from the left side, or head, of the list:

llist.appendleft("z")
print(llist)

print(llist.popleft())


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


print("-" * 50)
print('Self written linked lists')
llist = LinkedList()
print(llist)

first_node = Node("a")
llist.head = first_node
print(llist)

second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
second_node.next = third_node
print(llist)


class LinkedList:
    def __init__(self, nodes=None):
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
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def popleft(self):
        if not self.head:
            raise Exception('List is empty')
        val = self.head
        self.head = self.head.next
        return val

    def popright(self):
        if not self.head:
            raise Exception("List is empty")
        prev_node = self.head
        for node in self:
            if node.next is not None:
                prev_node = node
        val = node
        prev_node.next = None
        return val

    def add_last(self, node):
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def __getitem__(self, item):
        if not self.head:
            raise Exception('List is empty')

        if item == 0:
            return self.head

        node = self.head
        for i in range(1, item):
            node_value = node.next
        return node_value

    def get(self, item):
        return self.__getitem__(item)


print('-' * 50)
llist = LinkedList(["a", "d", "c", "Bb"])
print(llist)
print(list(iter(llist)))

for node in llist:
    print(node)
    
    
llist = LinkedList()
print(llist)

llist.add_first(Node("b"))
print(llist)

llist.add_first(Node("a"))
print(llist)


llist = LinkedList(["a", "b", "c", "d"])
print(llist)

llist.add_last(Node("e"))
print(llist)

llist.add_last(Node("f"))
print(llist)

print(llist[2])
print(llist.get(2))

print(llist)
print(llist.popleft())
print(llist)
print(llist.popright())
print(llist)