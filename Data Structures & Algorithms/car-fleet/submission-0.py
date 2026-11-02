class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        order = [(p,s) for p,s in zip(position,speed)]
        order.sort(reverse = True )
        fleets = []
        for p,s in order:
            t = (target-p)/s
            fleets.append(t)
            if len(fleets)>=2 and fleets[-1]<=fleets[-2] :
                fleets.pop()
        return len(fleets)    
                
