class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        tot = (n)*(n+1)//2
        add = 0
        for i in nums:
            add+=i
        return tot - add    
