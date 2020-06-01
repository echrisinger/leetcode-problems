class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = abs(x)
        new_x = 0
        while x:
            new_x *= 10
            new_x += x % 10
            x //= 10
        
        res = new_x * sign
        if res > (2**31 - 1) or res < -(2**31):
            res = 0

        return res

# O(1), O(1)
