class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        copy = nums.copy()
        i = 0
        j = len(nums)-1
        copy.sort()
        while i < j:
            sum = copy[i] + copy[j]
            if sum == target :
                if copy[i] == copy[j]:
                    idx1 = nums.index(copy[i])
                    idx2 = nums.index(copy[j],idx1+1)
                else:
                    idx1 =  nums.index(copy[i])   
                    idx2 = nums.index(copy[j])
                if idx1<idx2:
                    return [idx1,idx2]
                else:
                    return [idx2,idx1]    
            elif sum > target:  
                j -= 1
            else:
                i += 1    

            
        