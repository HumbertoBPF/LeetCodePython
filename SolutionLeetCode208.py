class Trie:

    def __init__(self):
        # pointer for the next letter of a word in the trie
        self.children = [None] * 26
        # flag indicating if the current node of a trie is the final node of a word
        self.isEndOfWord = False

    # Time complexity: O(n), where n is len(word)
    # Space complexity: O(1)
    def insert(self, word: str) -> None:
        current_node = self

        for letter in word:
            index = ord(letter) - ord("a")
            # Check if the current node already points to the current letter
            if current_node.children[index] is None:
                current_node.children[index] = Trie()

            current_node = current_node.children[index]
        # Set the final node as the end of a word
        current_node.isEndOfWord = True

    # Time complexity: O(n), where n is len(word)
    # Space complexity: O(1)
    def search_final_node_of_prefix(self, prefix: str):
        """
        Returns the node of the trie that represents the final letter of the specified prefix. It returns None if the
        prefix is not in the trie.
        """
        current_node = self

        for letter in prefix:
            index = ord(letter) - ord("a")
            current_node = current_node.children[index]
            # The current node doesn't point to the current letter
            if current_node is None:
                return None

        return current_node

    # Time complexity: O(n), where n is len(word)
    # Space complexity: O(1)
    def search(self, word: str) -> bool:
        final_node = self.search_final_node_of_prefix(word)
        # We found the word if the final node is not None and if it marks the end of a word
        return (final_node is not None) and final_node.isEndOfWord

    # Time complexity: O(n), where n is len(word)
    # Space complexity: O(1)
    def startsWith(self, prefix: str) -> bool:
        final_node = self.search_final_node_of_prefix(prefix)
        # Different from the search method, we don't care about the final node marking the end of a word
        return final_node is not None

trie = Trie()
print(trie.insert("apple"))
print(trie.search("apple"))   # return True
print(trie.search("app"))     # return False
print(trie.startsWith("app")) # return True
print(trie.insert("app"))
print(trie.search("app"))     # return True