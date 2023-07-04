from queue import Queue
class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class BinaryTree:
    index = -1

    def construct_tree(self, arr):

        self.index += 1
        if self.index >= len(arr) or arr[self.index] == -1:
            return None

        new_node = Node(arr[self.index])
        new_node.left = self.construct_tree(arr)
        new_node.right = self.construct_tree(arr)

        return new_node

    def preorder_traversal(self,root):
        if root == None:
            return

        print(root.val,end=" ")
        self.preorder_traversal(root.left)
        self.preorder_traversal(root.right)

    def inorder_traversal(self,root):

        if root == None:
            return

        self.inorder_traversal(root.left)
        print(root.val, end=" ")
        self.inorder_traversal(root.right)

    def bfs(self, root):

        if root == None:
            return

        queue = Queue()
        queue.put(root)
        queue.put(None)

        while not queue.empty():
            curr_node = queue.get()

            if curr_node == None:
                print()

                if not queue.empty():
                    queue.put(None)

                else:
                    break

            else:
                print(curr_node.val, end=" ")

                if curr_node.left != None:
                    queue.put(curr_node.left)

                if curr_node.right != None:
                    queue.put(curr_node.right)


if __name__ == '__main__':
    node = [1, 2, 4, -1, -1, 5, -1, 1, 3, -1, 6, -1, -1]
    tree = BinaryTree()
    root = tree.construct_tree(node)
    tree.preorder_traversal(root)
    print()
    print( tree.inorder_traversal(root))
    print()
    tree.bfs(root)

    # print(root.val)
    # print(tree.preorder_traversal(root).val)
