# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sametree(s,t):
            if not  s and not t:
                return True
            if not s or not t or s.val!=t.val:
                return False
            return sametree(s.right,t.right) and sametree(s.left,t.left)
        
        if not root:
            return False
        
        if sametree(root,subRoot):
            return True
        return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)
        