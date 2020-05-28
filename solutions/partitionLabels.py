from collections import defaultdict

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        char_ends = self.get_char_ends(S)
        active = set()
        res = []
        start = 0
        for end, c in enumerate(S):
            active.add(c)
            if char_ends[c] == end:
                active.remove(c)
            if not active:
                res.append(end-start+1)
                start = end+1
        return res
    
    def get_char_ends(self, S):
        ends_map = defaultdict(int)
        for i, c in enumerate(S):
            ends_map[c] = i
        
        return ends_map

# O(n) time, O(1) space (bc limited input)

