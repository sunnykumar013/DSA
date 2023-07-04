import queue


class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class BinaryTree:
    index = -1

    def construct_binary_tree(self, arr):
        self.index += 1
        if self.index >= len(arr) or arr[self.index] == -1:
            return
        new_node = Node(arr[self.index])
        new_node.left = self.construct_binary_tree(arr)
        new_node.right = self.construct_binary_tree(arr)
        return new_node

    def lfs_traversal(self, root):
        if root is None:
            return

        q = queue.Queue()
        q.put(root)
        q.put(None)

        while not q.empty():
            node = q.get()
            if node is None:
                print()  # Print a newline character to indicate the end of the level
                if not q.empty():
                    q.put(None)  # Append None to the queue to mark the end of the next level
            else:
                print(node.val, end=" ")  # Print the value of the current node
                if node.left:
                    q.put(node.left)  # Enqueue the left child
                if node.right:
                    q.put(node.right)  # Enqueue the right child


if __name__ == '__main__':
    nodes = [1, 2, 4, -1, -1, 5, -1, 1, 3, -1, 6, -1, -1]
    tree = BinaryTree()
    root = tree.construct_binary_tree(nodes)
    # print(root.val)
    tree.lfs_traversal(root)
