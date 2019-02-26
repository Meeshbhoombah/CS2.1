
import time
from pprint import pprint

class Node(object):

    def __init__(self, value):
        self.value = value
        self.count = 1
        self.children = {}
        self.data = None
    

class Trie(object):
    
    def __init__(self, corpus = None):
        self.root = Node("")

        if corpus is not None:
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
        words = []

        if node.data:
            words += [node.data]

        children = node.children.keys()
        if len(children) == 0:
            return words
           
        for char in children:
            words += self._collect(node.children[char])
        
        return words

    
    def search(self, prefix):
        """Returns all words beginning with the given prefix."""
        prefix = prefix.lower()

        node = self.root
        for char in prefix:
            try:
                node = node.children[char]
            except KeyError:
                break # return words up to the last found char

        return self._collect(node)

    
if __name__ == "__main__":
    from autocomplete import get_lines
    words = get_lines()

    a, start_of_assembly = Trie(), time.time()
    for word in words:
        a.insert(word)

    end_of_assembly = time.time()
    print("Assembled trie in", end_of_assembly - start_of_assembly)

    results, start_search = a.search("ass"), time.time()
    end_search = time.time()
    
    print("Completed search in", end_search - start_search)
    print(results[:10])

