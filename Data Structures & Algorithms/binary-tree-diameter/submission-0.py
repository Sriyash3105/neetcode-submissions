# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        max_diameter = 0
        queue = deque([root])
        
        while queue:
            node = queue.popleft()

            left_depth = self.depth(node.left)
            right_depth = self.depth(node.right)
            
            current_diameter = left_depth + right_depth
            
            max_diameter = max(max_diameter, current_diameter)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return max_diameter

     
    def depth(self,node):
        if not node:
            return 0
        
        return max(self.depth(node.right),self.depth(node.left)) + 1        