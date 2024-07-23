from typing import List

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None]*26
    # Let len(prefix) = n and the tree depth to be m
    # Time complexity: O(n*m)
    # Space complexity: O(m) (recursion stack)
    def suggest_products(self, search_word):
        output = []

        current_node = self
        prefix = ""
        # O(n)
        for letter in search_word:
            letter_index = ord(letter) - ord("a")

            current_node = current_node if (current_node is None) else current_node.children[letter_index]

            if current_node is None:
                output.append([])
                continue

            words = []
            prefix += letter
            # O(m)
            self.get_three_first_words(current_node, words, prefix)
            output.append(words)

        return output

    def get_three_first_words(self, trie_node, words, current_word):
        if len(words) == 3:
            return

        if trie_node.is_end:
            words.append(current_word)

        children = trie_node.children

        for i in range(26):
            child_node = children[i]

            if child_node is not None:
                current_char = chr(ord("a") + i)
                self.get_three_first_words(child_node, words, current_word + current_char)

    # Let n = len(word)
    # Time complexity: O(n)
    # Space complexity: O(1)
    def insert(self, word):
        current_node = self

        for letter in word:
            letter_index = ord(letter) - ord("a")

            if current_node.children[letter_index] is None:
                current_node.children[letter_index] = TrieNode()

            current_node = current_node.children[letter_index]

        current_node.is_end = True


class Solution:
    # Let len(products) = n, the maximum length of a product name = m, len(searchWord) = k
    # Time complexity: O(n*m + k*m) = O((n + k)*m)
    # Space complexity: O(m + nb_trie_nodes) (due to the call to the method get_suggested_products)
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = TrieNode()
        # O(n)
        for product in products:
            # O(m)
            trie.insert(product)
        # O(k*m)
        return trie.suggest_products(searchWord)
