# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.idx_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0                     
        return self.build(preorder, 0, len(inorder) - 1)

    def build(self, preorder, left, right):
        if left > right:
            return None

        root_val = preorder[self.pre_idx]
        self.pre_idx += 1
        node = TreeNode(root_val)

        mid = self.idx_map[root_val]

        node.left  = self.build(preorder, left, mid - 1)
        node.right = self.build(preorder, mid + 1, right)

        return node