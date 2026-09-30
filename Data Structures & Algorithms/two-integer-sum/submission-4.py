class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = dict()
        for i,e in enumerate(nums):
            if target -e in store:
                return [store[target-e],i]
            store[e] = i    

            
                
            
               