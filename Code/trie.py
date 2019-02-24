
from pprint import pprint

class Node(object):

    def __init__(self, value):
        self.value = value
        self.leaf = False
        self.children = {}
    

class Trie(object):
    
    def __init__(self, corpus):
        self.root = Node("")
        for word in corpus:
            word.lower()
            self.insert(word)

        pprint(self.root.children)


    def insert(self, word):
        if word is None or len(word) < 1:
            raise ValueError("Cannot pass empty word into the Trie.")

        root = self.root

        pprint(word)
        for char in word:
            try:
                root = root.children[char]
                print("Found ", root.value)
            except KeyError:
                print(root.children[char] = Node(char))
                root = root.children[char]
                print("Created ", root.value)

        root.leaf = True


    def delete(self, word):
        wordl = [] # nodes to be deleted

        root = self.root
        for char in word:
            root = root.children[char]

            if root.children == 1:
                wordl += root

        for node in reversed(wordl):
            print(node)
            del node


if __name__ == "__main__":
    autocomplete = Trie(["ape", "apple", "drape", "can", "cannot"])
