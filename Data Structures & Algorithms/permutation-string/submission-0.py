class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        k = len(s1)    
        window1 = defaultdict(int)
        window2 = defaultdict(int)    
        for ch in s1:
            window1[ch]+=1
        for ch in s2[:k]:
            window2[ch]+=1
        l,r = 0,k-1
        while r<len(s2):
            if window1 == window2:
                return True
            if r == len(s2)-1:
                return False    
            window2[s2[l]]-=1
            if window2[s2[l]] == 0:
                del window2[s2[l]]
            l+=1
            r+=1
            window2[s2[r]]+=1
        return False


                