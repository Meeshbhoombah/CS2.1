
from pprint import pprint

class Node(object):

    def __init__(self, value):
        self.value = value
        self.count = 1
        self.children = {}
        self.data = None
    

class Trie(object):
    
    def __init__(self, corpus):
        self.root = Node("")
        for word in corpus:
            word.lower()
            self.insert(word)


    def insert(self, word):
        if word is None or len(word) < 1:
            raise ValueError("Cannot pass empty word into the Trie.")

        node = self.root
        for char in word:
            try:
                node = node.children[char]
                node.count += 1
            except KeyError:
                n = Node(char)
                node.children[char] = n
                node = n

        node.data = word


    def delete(self, word):
        wordl = [] # nodes to be deleted

        node = self.root
        for char in word:
            parent = node
            node = node.children[char]

            if node.count == 1:
                wordl += [node]
                parent.children.pop(char)
            else:
                node.count -= 1

        for node in reversed(wordl):
            del node


    def  _collect(self, node):
        """Recursively walks all possible paths to collect words starting at 
        the given node."""
#        print(node.value)
        words = []

        if node.data:
            words += [node.data]
            print(words)

        children = node.children.keys()
        if len(children) == 0:
            return words
           
        for char in children:
            words += self._collect(node.children[char])


    def search(self, prefix):
        """Returns all words beginning with the given prefix."""
        node = self.root
        for char in prefix:
            try:
                node = node.children[char]
            except KeyError:
                break # return words up to the last found char

        return self._collect(node)

    
if __name__ == "__main__":
    autocomplete = Trie(["ape", "apple", "drape", "can", "cannot"])
    words = autocomplete.search("can")
    print(words)
