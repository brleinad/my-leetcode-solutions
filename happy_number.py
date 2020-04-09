# https://leetcode.com/problems/happy-number/


class Solution:
    def isHappy(self, n: int) -> bool:
        
        cycle = []
        while True:
            total = 0
            for digit in list(str(n)): 
                digit = int(digit)
                total += digit**2
            if total == 1:
                return True
            if n in cycle:
                return False
            cycle.append(n)
            n = total
