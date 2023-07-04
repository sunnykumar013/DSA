class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    index = -1

    def constructBinary(self, nodearr):
        self.index += 1

        if self.index >= len(nodearr) or nodearr[self.index] == -1:
            return None

        new_node = Node(nodearr[self.index])
        new_node.left = self.constructBinary(nodearr)
        new_node.right = self.constructBinary(nodearr)

        return new_node


if __name__ == '__main__':
    node = [1, 2, 4, -1, -1, 5, -1, 1, 3, -1, 6, -1, -1]
    tree = BinaryTree()
    root = tree.constructBinary(node)

    print(root.val)


