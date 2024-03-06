
class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end_of_string = False
    

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    def insertString(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if not node:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.end_of_string = True
        print ("success")
    
    def searchString(self, word):
        current = self.root
        for i in word:
            node = current.children.get(i)
            if not node:
                return False
            current = node
        return True if current.end_of_string else False
    
    def deleteString(self, root, word, index):
        ch = word[index]
        current = root.children.get(ch)
        deleted_node = False
        if len(current.children) > 1:
            self.deleteString(current, word, index + 1)
            return False
        if index == len(word) - 1:
            if len(current.children) >= 1:
                current.end_of_string = False
                return False
            else:
                root.children.pop(ch)
                return True
        if current.end_of_string == True:
            self.deleteString(current, word, index + 1)
            return False
        deleted_node = self.deleteString(current, word, index + 1)
        if deleted_node:
            root.children.pop(ch)
            return True
        else:
            return False
newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Appl")
newTrie.deleteString("App", 0)

print (newTrie.searchString("App"))
