class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def construct_tree(self, preorder, inorder):
        if not preorder or not inorder:
            return

        root = Node(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.construct_tree(preorder[1:mid+1], inorder[:mid])
        root.right = self.construct_tree(preorder[mid+1: ], inorder[mid+1: ])

        return root



if __name__ == "__main__":
    preorders =[3,9,20,15,7]
    inorders =[9,3,15,20,7]

    tree = BinaryTree()
    root = tree.construct_tree(preorders, inorders)
    print(root.val)