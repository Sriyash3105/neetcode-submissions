class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        store = defaultdict(int)
        window_size = 0
        max_frequency = 0
        while r<len(s): 
            store[s[r]]+=1
            window_size+=1
            max_frequency = max(max_frequency,store[s[r]])
            r+=1

            while window_size-max_frequency > k:
                window_size-=1
                store[s[l]]-=1
                l+=1

               
        return window_size     

