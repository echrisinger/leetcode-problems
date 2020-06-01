from collections import defaultdict, Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return t
        
        missing_counts = Counter(t)
        t = set(t)
        res = ""
        
        start = 0
        for end in range(len(s)):
            c = s[end]
            if c in missing_counts:
                missing_counts[c] -= 1
                if c in t and missing_counts[c] <= 0:
                    t.remove(c)
                
                while start <= end and\
                      (s[start] not in missing_counts or missing_counts[s[start]] < 0):
                    if s[start] in missing_counts:
                        missing_counts[s[start]] += 1
                    start += 1
                                    
                if not t and\
                   (not res or len(res) > len(s[start:end+1])):
                    res = s[start:end+1]
        
        return res

# O(n) time, O(n) space
