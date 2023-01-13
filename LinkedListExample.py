class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def prepend(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        if self.is_empty():
            self.tail = new_node
        self.size += 1

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and not found:
            if current.data == data:
                found = True
            else:
                previous = current
                current = current.next
        if found:
            if previous is None:
                self.head = current.next
            else:
                previous.next = current.next
            self.size -= 1
        else:
            raise ValueError("Data not in list")

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __repr__(self):
        return " -> ".join(str(item) for item in self)
