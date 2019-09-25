from labb3.bintreeFile import BinTree
from labb2.LinkedQFile import LinkedQ


def makechildren(startord):
    word_letters = list(startord)
    alphabet = "abcdefghijklmnopqrstuvwxyzåäö"
    gamla = BinTree()

    i = 0
    while i < len(startord):
        for letter in alphabet:
            word_letters[i] = letter
            try_word = "".join(word_letters)
            if (try_word != startord) and (try_word in svenska_ord) and (try_word not in gamla):
                gamla.put(try_word)
                print(try_word)
        word_letters = list(startord)
        i += 1

    return gamla


def makechildrenpath(startord, slutord, queue):
    alphabet = "abcdefghijklmnopqrstuvwxyzåäö"
    word_letters = list(startord)

    i = 0
    while i < len(startord):
        for letter in alphabet:
            word_letters[i] = letter
            try_word = "".join(word_letters)

            if try_word == slutord:
                print("Det finns en väg till", slutord)
                return True

            elif try_word != startord:
                if try_word in svenska_ord and try_word not in oldies_but_goodies:
                    queue.enqueue(try_word)
                    oldies_but_goodies.put(try_word)
        word_letters = list(startord)
        i += 1

    return False

def get_swedish_words():
    svenska = BinTree()
    with open("word3.txt", "r", encoding="utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()
            if ordet in svenska:
                pass
            else:
                svenska.put(ordet)

    return svenska


svenska_ord = get_swedish_words()
oldies_but_goodies = BinTree()

def run_ver_1(start):
    makechildren(start)

def run_ver_2(start, end, queue):
    queue.enqueue(start)
    makechildrenpath(start, end, queue)

    while not queue.is_empty():
        node = queue.dequeue()
        child_found = makechildrenpath(node, end, queue)

        if not child_found and queue.is_empty():
            print("Ingen väg hittades :(")
        elif child_found:
            break


def main():
    start_ord = input("Startord: ")
    run_ver_1(start_ord)
    slut_ord = input("Slutord: ")

    q = LinkedQ()

    run_ver_2(start_ord, slut_ord, q)



if __name__=="__main__":
    main()

