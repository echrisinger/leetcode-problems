class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            counts = [0]*10
            new_n = 0
            while n:
                val = (n  % 10)
                counts[val] += 1
                new_n += val**2
                n //= 10
            
            counts = tuple(counts)
            if counts in seen:
                return False
            seen.add(tuple(counts))
            n = new_n
        
        return True

# I have no clue what time or space...
