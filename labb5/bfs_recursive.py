from labb3.bintreeFile import BinTree
from labb2.LinkedQFile import LinkedQ
import sys

queue = LinkedQ()


class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent


def makechildrenpath(nod, start, end):
    alphabet = "abcdefghijklmnopqrstuvwxyzåäö"
    word_letters = list(nod.word)

    i = 0
    while i < len(word_letters):
        for letter in alphabet:
            word_letters[i] = letter
            try_word = "".join(word_letters)

            if try_word == end:
                print("Det finns en väg mellan " + start + " och " + try_word)
                writechain(ParentNode(try_word, nod))
                sys.exit()

            if try_word in svenska_ord and try_word not in oldies_but_goodies:
                word_node = ParentNode(try_word, nod)
                queue.enqueue(word_node)
                oldies_but_goodies.put(try_word)
        word_letters = list(nod.word)
        i += 1

    return False

def get_swedish_words():
    svenska = BinTree()
    with open("word3.txt", "r", encoding="utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()
            if ordet not in svenska:
                svenska.put(ordet)

    return svenska


svenska_ord = get_swedish_words()
oldies_but_goodies = BinTree()


def writechain(node):
    if node.parent:
        writechain(node.parent)
    print(str(node.word))

def main():
    start = input("Startord: ")
    end = input("Slutord: ")

    start_node = ParentNode(start)

    oldies_but_goodies.put(start_node.word)

    queue.enqueue(start_node)

    while not queue.is_empty():
        node = queue.dequeue()
        makechildrenpath(node, start, end)

    # Om man nått denna punkt finns det ingen väg
    print("Det finns ingen väg")



if __name__=="__main__":
    main()

