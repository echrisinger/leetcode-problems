from collections import defaultdict, Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        count_words = defaultdict(list)
        for word, count in counts.items():
            count_words[count].append(word)
            
        res = []
        for count in range(len(words), 0, -1):
            if count in count_words:
                for word in sorted(count_words[count]):
                    res.append(word)
                
                    if len(res) == k:
                        return res

        return res

# Actually non-optimal, as the last step is O(n^2), but practically speaking is faster in LC :P.
# For better asymptotic runtime, use a Priority Queue
