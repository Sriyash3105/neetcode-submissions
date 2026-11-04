class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        seen = set()
        size = 0
        maxsize = 0
        
        while r<len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
                size-=1
            seen.add(s[r])
            size+=1
            maxsize = max(maxsize,size)  
            r+=1
        return maxsize            