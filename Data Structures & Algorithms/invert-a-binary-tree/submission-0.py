# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        
        q = deque([root])
        

        while q:
            node = q.pop()

            if node.left :
                print(node.left.val)
                q.append(node.left)
                node_left= node.left
            if node.right :
                q.append(node.right)
                node_right = node.right
            
            node.left, node.right = node.right, node.left

        return root
            
            