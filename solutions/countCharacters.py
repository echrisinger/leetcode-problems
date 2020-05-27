class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counts = self.to_counts(chars)
        res = 0
        for word in words:
            word_counts = self.to_counts(word)
            added_counts = self.subtract(counts, word_counts)
            if self.is_valid(added_counts):
                res += len(word)
        
        return res
    
    def is_valid(self, tup):
        return not any([n < 0 for n in tup])

    def subtract(self, tup1, tup2):
        res = []
        for i in range(len(tup1)):
            res.append(tup1[i] - tup2[i])
        return tuple(res)
    
    def to_counts(self, s):
        counts = [0]*26
        for c in s:
            counts[self.to_i(c)] += 1
            
        return tuple(counts)

    def to_i(self, char):
        return ord(char) - ord('a')

# O(w*maxlen(w) + c) time, O(maxlen(w) + c) space
