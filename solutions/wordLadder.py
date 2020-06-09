from queue import Queue

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        sz = len(endWord)
        
        queue = Queue()
        queue.put((len(wordList), 1))
        wordList.append(beginWord)
        
        word_groups = {
            i: defaultdict(list)
            for i in range(sz)
        }
        for idx, word in enumerate(wordList):
            for i in range(sz):
                new_word = word[:i] + word[i+1:]
                word_groups[i][new_word].append(idx)
        
        seen = set()
        seen.add(beginWord)
        while queue.qsize():
            idx, length = queue.get()
            if wordList[idx] == endWord:
                return length
            
            seen.add(idx)    
            word = wordList[idx]
            for i in range(sz):
                new_word = word[:i] + word[i+1:]
                other_words = word_groups[i][new_word]
                for idx in other_words:
                    if idx in seen:
                        continue
                    seen.add(idx)
                    queue.put((idx, length+1))
        
        return 0

# O(len(word)*wordList) time, space
