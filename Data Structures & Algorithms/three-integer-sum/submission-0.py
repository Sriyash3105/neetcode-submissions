class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res =[]
        for i,e in enumerate(nums):
            if e > 0:
                break

            if i > 0 and e == nums[i - 1]:
                continue
            l = i+1
            r = n-1
            
            while l<r:
                sum = e+nums[l]+nums[r]
                if sum > 0:
                    r-=1
                elif sum < 0:
                    l+=1
                else:
                    res.append([e,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1] :
                        l+=1
        return res                       
                