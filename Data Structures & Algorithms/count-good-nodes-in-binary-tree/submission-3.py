# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)
        
    def dfs(self, node, current_max):
        if not node:
            return 0
        good = 1 if node.val >= current_max else 0
        new_max = max(current_max, node.val)
        left = self.dfs(node.left, new_max)
        right = self.dfs(node.right, new_max)
        return good + left + right