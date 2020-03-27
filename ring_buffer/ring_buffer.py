from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) >= self.capacity:
            self.current.value = item
            if self.current.next is None:
                self.current = self.storage.head
            else:
                self.current = self.current.next
        else:
            self.storage.add_to_tail(item)
            if len(self.storage) == self.capacity:
                self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        node = self.storage.head

        while node is not None:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None] * capacity

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.current] = item
        self.current += 1
        if self.current >= self.capacity:
            self.current = 0

    def get(self):
        return [item for item in self.storage if item is not None]
