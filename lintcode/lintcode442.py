class Trie:

    def __init__(self):
        # do intialization if necessary
        self.root = Node(False)

    """
    @param: word: a word
    @return: nothing
    """

    def insert(self, word):
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.next_nodes[idx] == None:
                node.next_nodes[idx] = Node()
            node = node.next_nodes[idx]
        node.can_end = True

    """
    @param: word: A string
    @return: if the word is in the trie.
    """

    def search(self, word):
        node = self.find_last_node(self.root, word)
        if node == None:
            return False
        return node.can_end

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """

    def startsWith(self, prefix):
        node = self.find_last_node(self.root, prefix)
        if node == None:
            return False
        return True

    def find_last_node(self, node, word):
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.next_nodes[idx] == None:
                return None
            node = node.next_nodes[idx]
        return node


class Node:
    def __init__(self, can_end=False):
        self.next_nodes = [None] * 26
        self.can_end = can_end


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    """
    @param: word: a word
    @return: nothing
    """

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def find(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return None
        return node

    """
    @param: word: A string
    @return: if the word is in the trie.
    """

    def search(self, word):
        node = self.find(word)
        return node is not None and node.is_word

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """

    def startsWith(self, prefix):
        return self.find(prefix) is not None