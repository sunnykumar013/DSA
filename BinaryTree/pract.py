class Node:
    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None

class Tree:
    # res =[]

    def construct_tree(self, preorder, inorder):

        if not preorder or not inorder:
            return

        root = Node(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.construct_tree(preorder[1 : mid+1], inorder[:mid])
        root.right = self.construct_tree(preorder[mid+1:], inorder[mid+1: ])

        return root

    def traversal(self,root, n, res):

        if root is None:
            return


        if root.val == n:
            res.append(root.val)
            return  True



        if root.val != n and (self.traversal(root.left,n, res) or self.traversal(root.right, n,res)):
            # print(root.val != n and (self.traversal(root.left,n) or self.traversal(root.right, n)))
            res.append(root.val)
            return True





        return res



    # def traversal(self,root, n):
    #
    #     if root is None:
    #         return
    #
    #     print(root.val, end=" ")
    #     self.traversal(root.left)
    #     self.traversal(root.right)
    #
    #     return root


if __name__ == '__main__':
    tree = Tree()
    preorder =['A', 'B', 'D', 'E', 'C', 'F']
    inorder = ['D', 'B', 'E', 'A', 'F', 'C']

    root = tree.construct_tree(preorder, inorder)
    res =[]
    r=[]
    s = tree.traversal(root, 'E', res)
    rt = tree.traversal(root, 'F', r)
    print(res)
    print(r)