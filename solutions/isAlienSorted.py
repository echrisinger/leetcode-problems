class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {
            c: i
            for i, c in enumerate(order)
        }
        for i in range(1, len(words)):
            score = self.to_score(words[i], rank)
            prev_score = self.to_score(words[i-1], rank)
            
            for j in range(len(score)):
                if j >= len(prev_score) or score[j] > prev_score[j]:
                    break
                elif prev_score[j] > score[j]:
                    print(prev_score[j], score[j])
                    return False
            else:
                return False
            
        return True
    
    def to_score(self, word, rank):
        res = []
        for c in word:
            res.append(rank[c])
        
        return res

# O(n) time, O(n) space
