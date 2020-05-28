
class TrieNode:
    def __init__(self, val):
        self.val = val
        self.is_word = False
        self.children = {}
        
class Trie:
    def __init__(self):
        self.root = TrieNode('')
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode(c)
            
            curr = curr.children[c]
        
        curr.is_word = True
    
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for word in products:
            trie.insert(word)
        
        res = []
        curr = trie.root
        prev = []
        
        for i,c in enumerate(searchWord):
            if curr and c in curr.children:
                curr = curr.children[c]
                suggestions = self.dfs_trie(curr, prev)
            else:
                curr = None
                suggestions = []
                
            res.append(suggestions)
            prev.append(c)
            
        return res
                    
        
    def dfs_trie(self, node, prev):
        prev.append(node.val)
        res = []
        if node.is_word:
            res.append(''.join(prev))
        
        for i in range(26):
            char = chr(ord('a')+i)
            if char not in node.children:
                continue
                
            child = node.children[char]
            if len(res) == 3:
                break
            words = self.dfs_trie(child, prev)
            for w in words[:3-len(res)]:
                res.append(w)
                
        prev.pop()
        return res

# if searchWord = aaaaa...
# products = [aaaaaaaa....a, aaaaa...ab, aaaaaa....ac]
# each round of DFS could take O(products).
# performed for each character in searchWord
# so total time: O(p*s)
# space: O(products + s*products) because Trie takes up space
# of products and each char could have the space of products
# as in the above example.

