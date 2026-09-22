# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if not root :
            return 
        if p.val > q.val:
            pp , qq = q , p
        else : 
            pp = p
            qq = q
             
        if root.val >= pp.val and root.val <= qq.val:
            return root
        if root.val == pp.val :
            return pp
        if root.val == qq.val:
            return qq
        
        if pp.val >= root.val and qq.val >= root.val:
            return self.lowestCommonAncestor(root.right,pp,qq)

        if pp.val <= root.val and qq.val <= root.val:
            return self.lowestCommonAncestor(root.left,pp,qq)
        
         


        