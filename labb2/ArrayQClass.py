from array import array


class ArrayQ:

    def __init__(self):
        self._buffer = array('i')

    def enqueue(self, i):
        self._buffer.append(i)

    def dequeue(self):
        return self._buffer.pop(0)

    def is_empty(self):
        if len(self._buffer) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self._buffer)


if __name__ == "__main__":
    q = ArrayQ()
    q.enqueue(1)
    q.enqueue(2)
    x = q.dequeue()
    y = q.dequeue()
    if (x == 1 and y == 2):
        print("OK")
    else:
        print("FAILED")
