# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        r1 = []
        r2 = []

        res1 = self.path(root, p, r1)
        res2 = self.path(root, q, r2)
        # print(r1)
        # print(r2)

        i = len(r1) - 1
        j = len(r2) - 1
        while i >= 0 and j >= 0:
            if r1[i] != r2[j]:
                break
            i -= 1
            j -= 1

        # print(r1[i+1])

        return r1[i + 1]

    def path(self, root, n1, res):
        # print("rs",res,n1.val)
        if root is None:
            return

        if root.val == n1.val:
            res.append(root)
            return True

        if root.val != n1.val and (self.path(root.left, n1, res) or self.path(root.right, n1, res)):
            res.append(root)
            return True

        return res


