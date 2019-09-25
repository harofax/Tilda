from labb2.LinkedQFile import LinkedQ as Queue
#from labb2.ArrayQClass import ArrayQ as Queue

cards = input("I vilken ordning ligger korten i?\n").split()
cards = [int(i) for i in cards]

magicQ = Queue()

for card in cards:
    magicQ.enqueue(card)


def perform_magic(magic_queue):
    result = list()

    while not magic_queue.is_empty():
        magic_queue.enqueue(magic_queue.dequeue())
        result.append(magic_queue.dequeue())

    [print(i, end=" ") for i in result]


perform_magic(magicQ)
