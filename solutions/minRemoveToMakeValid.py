class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        to_remove = set()
        for i,c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)
        
        to_remove = to_remove.union(set(stack))
        res = []
        for i, c in enumerate(s):
            if i in to_remove:
                continue
            res.append(c)
        
        return ''.join(res)
            
# O(n) time, space
