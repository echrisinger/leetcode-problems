DIG_MAP = {
    2: ['a','b','c'],
    3: ['d','e','f'],
    4: ['g','h','i'],
    5: ['j','k','l'],
    6: ['m','n','o'],
    7: ['p','q','r','s'],
    8: ['t','u','v'],
    9: ['w','x','y','z'],
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digits = [int(d) for d in list(digits)]
        res = []
        def backtrack(idx, path) -> List[str]:
            if idx == len(digits):
                res.append(''.join(path))
                return

            dig = digits[idx]
            for c in DIG_MAP[dig]:
                path.append(c)
                backtrack(idx+1, path)
                path.pop()

        backtrack(0, [])
        return res
    
    
# O(4^d) time, space
