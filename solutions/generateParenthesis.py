class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.backtrack(n, n, [], res)
        return res
        
    def backtrack(self, open_count: int, close_count: int, path: List[str], res: List) -> List[str]:
        if open_count == 0 and close_count == 0:
            res.append(''.join(path))
            return
        
        if open_count:
            path.append('(')
            self.backtrack(open_count-1, close_count, path, res)
            path.pop()
            
        if close_count > open_count:
            path.append(')')
            self.backtrack(open_count, close_count-1, path, res)
            path.pop()

# O(2^n) time, space I believe
