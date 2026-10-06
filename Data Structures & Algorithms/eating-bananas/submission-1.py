class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = self.Max(piles)
        l = 1
        res = r
        while l <= r:
            m = (l+r)//2
            sum = 0
            for i in piles:
                sum += math.ceil(i/m)
            if sum <= h:
                res = m
                r = m-1
            else:
                l = m+1
        return res        



    def Max(self,arr : List[int]):
        maxi = arr[0]
        for i in arr:
            maxi = max(i,maxi)
        return maxi    
               