class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n-1
        if target == nums[0]:
            return 0
        if target == nums[n-1]:
            return n-1
        for i in range(n-1):
            mid  = (low +high)//2
            if nums[mid] > target:
                high = mid -1
            elif nums[mid] < target:
                low = mid + 1
            else: 
                return mid

        return -1            