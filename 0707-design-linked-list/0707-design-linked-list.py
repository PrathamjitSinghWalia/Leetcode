class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        current = self.head

        for _ in range(index):
            current = current.next

        return current.val

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

        self.size += 1

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
            return

        if index == self.size:
            self.addAtTail(val)
            return

        current = self.head

        for _ in range(index):
            current = current.next

        newNode = Node(val)

        newNode.prev = current.prev
        newNode.next = current

        current.prev.next = newNode
        current.prev = newNode

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        if index == 0:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None

        elif index == self.size - 1:
            self.tail = self.tail.prev
            self.tail.next = None

        else:
            current = self.head

            for _ in range(index):
                current = current.next

            current.prev.next = current.next
            current.next.prev = current.prev

        self.size -= 1