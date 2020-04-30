import csv

with open('input_file.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    rows = list(csv_reader)
    N = int(rows[0][0])
    i = 1
    class BinomialTree:

        def __init__(self, key):
            self.key = key
            self.children = []
            self.order = 0

        def appendT(self, node):
            self.children.append(node)
            self.order = self.order + 1


    def buildBinomialHeap():
        H = BinomialHeap()
        return H


    class BinomialHeap:

        def __init__(self):
            self.trees = []

        def findMin(self):

            if not self.trees:
                return "Heap gol"
            else:
                min_root = self.trees[0].key
                for tree in self.trees:
                    if tree.key < min_root:
                        min_root = tree.key
                return min_root

        def deleteMin(self):
            if not self.trees:
                return "Heap gol"
            min_key = self.findMin()
            for tree in self.trees:
                if tree.key == min_key:
                    min_tree = tree
                    break
            self.trees.remove(min_tree)
            B = BinomialHeap()
            B.trees = min_tree.children
            self.merge(B)
            return min_tree.key

        def deleteElement(self, key):

            if not self.trees:
                return "Heap gol"

            else:
                key = self.findMin() - 1
                self.deleteMin()

        def merge(self, B):

            self.trees.extend(B.trees)
            sorted(self.trees, key=lambda tree: tree.order)

            if not self.trees:
                return "Heap gol"

            else:

                for i in range(len(self.trees) - 2):
                    crt = self.trees[i]
                    next = self.trees[i + 1]

                    if crt.order == next.order:
                        if crt.key < next.key:
                            crt.appendT(next)
                            del self.trees[i + 1]
                        else:
                            next.appendT(crt)
                            del self.trees[i]

        def insert(self, key):
            E = BinomialHeap()
            E.trees.append(BinomialTree(key))
            self.merge(E)

    H = buildBinomialHeap()
    while i <= N:
        if rows[i][0] == '1':
            H.insert(rows[i][1])
        elif rows[i][0] == '2':
            print(H.deleteElement(rows[i][1]))
        elif rows[i][0] == '3':
            print(H.findMin())
        elif rows[i][0] == '4':
            print(H.deleteMin())
        i = i+1


# previous test:
# B1 = BinomialHeap()
# B1.insert(3)
# B1.insert(2)
# B1.insert(1)
# B1.insert(4)
# B1.insert(7)
# B1.insert(90)
# B1.insert(99)
# B1.insert(19)
# B1.insert(0)
# print(B1.findMin())
# B1.deleteMin()
# print(B1.findMin())
# B1.deleteMin()
# print(B1.findMin())
# B1.deleteMin()
# B1.deleteElement(3)
# print(B1.findMin())
# B1.deleteElement(4)
# print(B1.findMin())
