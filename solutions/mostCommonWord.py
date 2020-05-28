from collections import Counter, defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        curr_word = []
        counts = defaultdict(int)
        max_count, max_word = 0, ''
        for c in paragraph:
            if c in " !?',;.":
                word = ''.join(curr_word).lower()
                if word not in banned and word:
                    counts[word] += 1
                    if counts[word] > max_count:
                        max_count, max_word = counts[word], word
                curr_word = []
            else:
                curr_word.append(c)
        
        word = ''.join(curr_word).lower()
        if word not in banned and word:
            counts[word] += 1
            if counts[word] > max_count:
                max_count, max_word = counts[word], word

        return max_word

# O(n) time, space
