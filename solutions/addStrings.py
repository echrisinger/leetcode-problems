class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        i1 = len(num1) - 1
        i2 = len(num2) - 1
        curr = 0
        while i1 >= 0 or i2 >= 0:
            if i1 >= 0:
                curr += int(num1[i1])
            if i2 >= 0:
                curr += int(num2[i2])
            
            res.append(curr % 10)
            curr //= 10
            
            i1 -= 1
            i2 -= 1
        
        if curr:
            res.append(curr)
        
        return ''.join([str(i) for i in res][::-1])

# CO PZ
# O(n1 + n2), O(maxlen(n1, n2))
