# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        print(root.val)
        if root.right == None and root.left == None:
            return 0
        if root.left: 
            self.maxDepth(root.left)
        if root.right:
            self.maxDepth(root.right)
        
        # total = self.maxDepth(root)
        # return total



a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)

a.left = b
a.right = c
c.left = d
c.right = e

sol = Solution()
sol.maxDepth(a)