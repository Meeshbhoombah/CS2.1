
from pprint import pprint

class Node(object):

    def __init__(self, value):
        self.value = value
        self.count = 1
        self.children = {}
        self.ldata = None
    

class Trie(object):
    
    def __init__(self, corpus):
        self.root = Node("")
        for word in corpus:
            word.lower()
            self.insert(word)


    def insert(self, word):
        if word is None or len(word) < 1:
            raise ValueError("Cannot pass empty word into the Trie.")

        root = self.root

        for char in word:
            try:
                root = root.children[char]
                root.count += 1
            except KeyError:
                node = Node(char)
                root.children[char] = node
                root = node 

        root.ldata = word


    def delete(self, word):
        wordl = [] # nodes to be deleted

        root = self.root
        for char in word:
            prev = root
            root = root.children[char]

            if root.count == 1:
                wordl += [root]
                prev.children.pop(char)
            else:
                root.count -= 1

        for node in reversed(wordl):
            del node


if __name__ == "__main__":
    autocomplete = Trie(["ape", "apple", "drape", "can", "cannot"])
