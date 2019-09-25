class Node:

    def __init__(self, value):
        self.value = value
        self.next_node = None


class LinkedQ:

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, x):
        new_node = Node(x)

        if self.last is not None:
            self.last.next_node = new_node
        else:
            self.first = new_node

        self.last = new_node
        self.size += 1

    def dequeue(self):
        if self.first.next_node:
            result = self.first
            self.first = self.first.next_node
            self.size -= 1
            return result.value
        else:
            result = self.first
            self.size -= 1
            return result.value

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def print_queue(self):
        current = self.first
        printlist = []
        while current:
            printlist.append(current.value)
            current = current.next_node
        print(printlist)

    def get_size(self):
        return self.size