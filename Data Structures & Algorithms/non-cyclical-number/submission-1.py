class Solution:
    def digit_square_sum(self,n:int):
        sum = 0
        while n:
            sum += (n%10)**2
            n = n // 10
        return sum    


    def isHappy(self, n: int) -> bool:
        store = set()

        while n not in store:
            store.add(n)
            n= self.digit_square_sum(n)
            if n == 1:
                return True
        return False    