class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count = 0
        res = [0]*len(nums)
        for i in nums:
            if i !=0:
                product = product*i
            else:
                count+=1
        if count > 1:
            return res
        elif count == 1:
            k = nums.index(0) 
            res[k] = product
            return res
        else:
            for i in range(len(nums)):
                res[i] = product//nums[i] 
            return res                     

               
        