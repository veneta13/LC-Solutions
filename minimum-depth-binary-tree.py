# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def DFS(self, current, root):
        if not root:
            return current

        if not root.left or not root.right:
            return max(self.DFS(current + 1, root.left), self.DFS(current + 1, root.right))

        return min(self.DFS(current + 1, root.left), self.DFS(current + 1, root.right))

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.DFS(0, root)
