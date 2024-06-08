class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        current_node = self.root

        for letter in word:
            index = ord(letter) - ord('a')
            # If the letter has not been added to the trie yet, do it
            if current_node.children[index] is None:
                current_node.children[index] = Trie()
            current_node = current_node.children[index]

        current_node.isEndOfWord = True

    def search(self, word: str) -> bool:
        return self.find_letter(self.root, 0, word)

    def find_letter(self, current_node, i, word):
        if current_node is None:
            return False

        if i == len(word):
            return current_node.isEndOfWord

        letter = word[i]
        children = current_node.children

        # A dot matches any letter, so we have to search in all the children
        if letter == ".":
            for child in children:
                if self.find_letter(child, i + 1, word):
                    return True
        # A non-dot character targets a specific child
        else:
            index = ord(letter) - ord("a")
            if self.find_letter(children[index], i + 1, word):
                return True

        return False