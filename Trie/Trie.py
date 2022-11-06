class TrieNode:

    # Link : https://youtu.be/ypR5GuZeO-o
    def __init__(self):
        self.children = dict()
        self.EOW = False


class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
        
            cur = cur.children[ch]
        
        cur.EOW = True
    
    def search(self,word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return False
            
            cur = cur.children[ch]
        
        return cur.EOW
    
    def startsWith(self,prefix):
        cur = self.root
        for ch in prefix:
            if ch not in cur.children:
                return False
            
            cur = cur.children[ch]
        
        return True


if __name__  == "__main__":

    obj  = Trie()
    obj.insert("apple")
    obj.insert("app")
    print(obj.search("app"))