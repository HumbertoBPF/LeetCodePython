class Node:
    def __init__(self, val, previous, next):
        self.val = val
        self.previous = previous
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.oldest = None # head of the doubly linked list
        self.newest = None # last item of the doubly linked list

    def get(self, key: int) -> int:
        existing_cache = self.cache.get(key)

        if existing_cache is None:
            return -1

        value = existing_cache[0]
        node = existing_cache[1]

        self.move_item_to_the_end_of_ddl(node)
        self.cache[key] = [value, self.newest]

        return value

    def put(self, key: int, value: int) -> None:
        existing_cache = self.cache.get(key)
        # Update an existing key
        if existing_cache is not None:
            node = existing_cache[1]
            self.move_item_to_the_end_of_ddl(node)
            self.cache[key] = [value, self.newest]
            return

        node = Node(key, None, None)
        # Dropping the oldest item when the capacity is exceeded
        if len(self.cache) >= self.capacity:
            self.drop_oldest_item()

        self.add_node_at_the_end_of_dll(node)
        self.cache[key] = [value, self.newest]

    def add_first_item(self, node):
        self.oldest = node
        self.newest = node

    def drop_oldest_item(self):
        if self.oldest is not None:
            new_oldest = self.oldest.next

            del self.cache[self.oldest.val]

            self.oldest.next = None

            if new_oldest is not None:
                new_oldest.previous = None

            self.oldest = new_oldest

    def add_node_at_the_end_of_dll(self, node):
        if self.newest is not None:
            self.newest.next = node

        node.previous = self.newest

        self.newest = node

        if self.oldest is None:
            self.oldest = node

    def move_item_to_the_end_of_ddl(self, node):
        previous_node = node.previous
        next_node = node.next
        # The item is already at the end of the ddl
        if next_node is None:
            return
        # Addressing case where the node is the head
        if previous_node is None:
            self.oldest = next_node
        else:
            previous_node.next = next_node

        next_node.previous = previous_node

        node.next = None
        node.previous = None
        # Adding removed item at the end of the dll
        self.add_node_at_the_end_of_dll(node)
