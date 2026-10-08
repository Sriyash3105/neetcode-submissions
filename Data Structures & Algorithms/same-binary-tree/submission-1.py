class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue1 = deque([p])
        queue2 = deque([q])    
        
        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            
            if not node1 and not node2:
                continue
                
            if not node1 or not node2 :
                return False

            if node1.val != node2.val:
                return False       
            queue1.append(node1.left)
            queue2.append(node2.left)
            queue1.append(node1.right)
            queue2.append(node2.right)
            
        return True