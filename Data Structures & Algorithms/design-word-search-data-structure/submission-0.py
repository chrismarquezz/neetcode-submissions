class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.is_end = False
    
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(j, node):
            if j == len(word):
                return node.is_end
            c = word[j]
            if c == ".":
                for child in node.children.values():
                    if dfs(j + 1, child):
                        return True
                return False
            else:
                if c not in node.children:
                    return False
                return dfs(j + 1, node.children[c])
                
        return dfs(0, self.root)