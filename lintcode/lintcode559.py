"""
Definition of TrieNode:
class TrieNode:
    def __init__(self):
        # <key, value>: <Character, TrieNode>
        self.children = collections.OrderedDict()
        self.top10 = []
"""


class TrieService:

    def __init__(self):
        self.root = TrieNode()

    def get_root(self):
        # Return root of trie root, and
        # lintcode will print the tree struct.
        return self.root

    # @param {str} word a string
    # @param {int} frequency an integer
    # @return nothing
    def insert(self, word, frequency):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            top10 = node.children[ch].top10
            top10.append(frequency)
            index = len(top10) - 1
            while index > 0:
                if top10[index - 1] >= top10[index]:
                    break
                top10[index], top10[index - 1] = top10[index - 1], top10[index]
                index -= 1

            # node.children[ch].top10.sort(reverse=True)
            while len(top10) > 10:
                top10.pop()

            node = node.children[ch]