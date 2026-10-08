class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
            
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            
            if node.val == subRoot.val:
                if self.Compare(node, subRoot):
                    return True
                    
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return False

    def Compare(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        if not node1 and not node2:
            return True
            
        if not node1 or not node2 or node1.val != node2.val:
            return False
            
        return self.Compare(node1.left, node2.left) and self.Compare(node1.right, node2.right)