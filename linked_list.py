class LinkedList:
    def __delitem__(self, key):
        assert isinstance(key, int)
        assert 0 <= key < self.size

        node = self.sentinel.next
        for _ in range(key):
            node = node.next
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def __init__(self):
        self.sentinel = Node(None)
        self.size = 0
        self.clear()

    def __iter__(self):
        node = self.sentinel.next
        while node is not self.sentinel:
            yield node.value
            node = node.next

    def __len__(self):
        return self.size

    def __repr__(self):
        return str(list(self))

    def append(self, item):
        new = Node(item, next_=self.sentinel, prev=self.sentinel.prev)
        new.prev.next = new
        self.sentinel.prev = new
        self.size += 1

    def clear(self):
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
        self.size = 0


class Node:
    def __init__(self, val, next_=None, prev=None):
        self.value = val
        self.next = next_
        self.prev = prev
