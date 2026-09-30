class Solution:
    def countBits(self, n: int) -> List[int]:
        sol = []
        for i in range(n+1):
            sol.append(self.count_1(i))
        return sol    
        
    def count_1(self,n : int):
        ans  = 0
        while n:
            ans+=n%2
            n = n//2
        return ans    
