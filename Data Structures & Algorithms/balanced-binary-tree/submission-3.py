class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.check_height(root) != -1
    
    def check_height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
            
        left_height = self.check_height(node.left)
        if left_height == -1:
            return -1  
            
        right_height = self.check_height(node.right)
        if right_height == -1:
            return -1  
            
        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1