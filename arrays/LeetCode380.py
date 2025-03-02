import random


# Space complexity: O(n)
class RandomizedSet:
    def __init__(self):
        self.randomized_set = {}
        self.items = []
    # Time complexity: O(1)
    def insert(self, val: int) -> bool:
        if val not in self.randomized_set:
            len_randomized_set = len(self.randomized_set)
            len_items = len(self.items)
            # If there are no Nones in the array "items", append the value and
            if len_randomized_set == len_items:
                self.items.append(val)
            # If there is at least one None in the array "items", store the value in the place of its first occurrence
            else:
                self.items[len_randomized_set] = val
            # Store the value index in "items" in the hash map
            self.randomized_set[val] = len_randomized_set

            return True

        return False
    # Time complexity: O(1)
    def remove(self, val: int) -> bool:
        if val in self.randomized_set:
            len_randomized_set = len(self.randomized_set)

            removed_index = self.randomized_set[val]

            last_value_from_items = self.items[len_randomized_set - 1]
            # Swap the item to be removed with the last item in the array.
            # Then, set the new last item (now, that holds the item to be removed) to None
            self.items[removed_index] = last_value_from_items
            self.items[len_randomized_set - 1] = None
            # Update indices in the hash map
            self.randomized_set[last_value_from_items] = removed_index
            del self.randomized_set[val]

            return True

        return False
    # Time complexity: O(1)
    def getRandom(self) -> int:
        n = len(self.randomized_set)
        random_index = random.randint(0, n - 1)
        return self.items[random_index]

