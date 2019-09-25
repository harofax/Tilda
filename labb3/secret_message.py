from labb3.bintreeFile import BinTree

svenska = BinTree()

with open("word3.txt", "r", encoding="utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()
        if ordet in svenska:
            print(ordet, end=" ")
        else:
            svenska.put(ordet)
print("\n")

english = BinTree()

with open("engelska.txt", "r", encoding="utf-8") as engfile:
    """
    Since file isn't formatted like swedish list, we need to both strip and split
    it to get each word separated
    """
    for row in engfile:
        row_words = row.strip().split()
        for word in row_words:

            if word in english:
                continue
            else:
                english.put(word)
                if word in svenska:
                    print(word, end=" ")