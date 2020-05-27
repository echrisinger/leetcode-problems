from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        seen_counts = defaultdict(int)
        total = 0
        for domino in dominoes:
            key = tuple(sorted(domino))
            total += seen_counts[key]
            seen_counts[key] += 1
            
        return total

# O(n) time, O(n) space

