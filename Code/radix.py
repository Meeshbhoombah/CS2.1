
from pprint import pprint

class Node(object):

    def __init__(self, value):
        self.value = value
        self.leaf = False
        self.children = {}
    

class Autocomplete(object):
    
    def __init__(self, corpus):
        self.root = Node("")
        for word in corpus:
            word.lower()
            self.insert(word)


    def insert(self, word):
        if word is None or len(word) < 1:
            raise ValueError("Cannot pass empty word into the Trie.")

        root = self.root

        try:
            for char in word:
                try:
                    root = root.children[char]
                except KeyError:
                    root = root.children[char] = Node(char)
        except IndexError:
            root.leaf = True


    def delete(self, word):
        wordl = [] # nodes to be deleted

        root = self.root
        for char in word:
            root = root[char]

            if root.uses == 1:
                wordl += root

        for node in wordl[::-1]:
            del node


if __name__ == "__main__":
    a = Autocomplete(["ape", "apple", "drape", "can", "cannot"])
