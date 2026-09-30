class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        store =  set()
        for i in nums:
            if i in store:
                store.remove(i)
            else:     
                store.add(i)
        ans = list(store)    
        return ans[-1]    
            