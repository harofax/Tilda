class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def has_left_child(self):
        return self.left

    def has_right_child(self):
        return self.right

    def is_leaf(self):
        return not (self.right or self.left)


class BinTree:
    def __init__(self):
        self.root = None

    def put(self, new_value):
        self.putta(self.root, new_value)

    def putta(self, root, value):
        if self.root is None:
            self.root = Node(value)
        else:
            if root.val > value:
                if root.left is None:
                    root.left = Node(value)
                else:
                    self.putta(root.left, value)

            else:
                if root.right is None:
                    root.right = Node(value)
                else:
                    self.putta(root.right, value)

    def __contains__(self, value):
        return self.finns(self.root, value)

    def finns(self, root, value):
        # Either the tree is empty, or we've reached the end of a branch
        if root is None:
            return False
        # Check if current node is what we're looking for
        elif root.val == value:
            return True
        # If not, we go to the left node and continue the search
        elif value < root.val:
            return self.finns(root.left, value)
        # Then the right node
        elif value > root.val:
            return self.finns(root.right, value)

    def write(self):
        self.skriv(self.root)
        print("\n")

    def skriv(self, root):
        # Means we have reached the end of the this path basically
        if root is None:
            return

        # By printing them like this, we always get them in
        # "inorder" order, since we always go through the values leftmost first
        # (which are the smallest)
        self.skriv(root.left)
        print(root.val)
        self.skriv(root.right)







def main():
    numTree = BinTree()

    numTree.put(10)
    numTree.put(5)
    numTree.put(15)
    numTree.put(8)
    numTree.put(9)
    numTree.put(6)
    numTree.put(1)
    numTree.put(11)
    numTree.put(20)

    numTree.write()

    print("5 in numtree?", 5 in numTree)
    print("23 in numtree?", 23 in numTree)

    print("----------------------------\n")
    # ----------------
    wordTree = BinTree()

    wordTree.put("gurka")
    wordTree.put("hejsan")
    wordTree.put("alfons")
    wordTree.put("zebra")
    wordTree.put("banan")
    wordTree.put("citron")
    wordTree.put("hjälm")

    wordTree.write()

    print("zebra in wordtree?", "zebra" in wordTree)
    print("pirat in wordtree?", "pirat" in wordTree)


if __name__=="__main__":
    main()