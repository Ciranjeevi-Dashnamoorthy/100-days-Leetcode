# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mapp={}
        for i in range(len(inorder)):
            mapp[inorder[i]]=i
        from collections import deque
        queue=deque(preorder)
        def helper(start,end):

            if start>end:
                return None
            root=TreeNode(queue.popleft())
            mid=mapp[root.val]

            root.left=helper(start,mid-1)
            root.right=helper(mid+1,end)

            return root

        return helper(0,len(mapp)-1)

    