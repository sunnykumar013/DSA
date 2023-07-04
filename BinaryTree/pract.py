class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    index = -1
    def construct_tree(self, node_arr):

        self.index += 1

        if self.index >= len(node_arr) or node_arr[self.index] == -1:
            return None

        new_node = Node(node_arr[self.index])

        new_node.left = self.construct_tree(node_arr)
        new_node.right = self.construct_tree(node_arr)

        return new_node

    def print_preorder(self, root):
        if root == None:
            return
        print(root.data,end=" ")
        self.print_preorder(root.left)
        self.print_preorder(root.right)

if __name__ == '__main__':
    node = [1, 2, 4, -1, -1, 5, -1, 1, 3, -1, 6, -1, -1]
    tree = BinaryTree()
    root = tree.construct_tree(node)
    tree.print_preorder(root)

    # print(root.data)



