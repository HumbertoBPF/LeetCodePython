class MyCalendar:
    def __init__(self):
        self.books = set()


    def book(self, start: int, end: int) -> bool:
        if (start, end) in self.books:
            return False

        for book in self.books:
            book_start, book_end = book
            # The intervals intersect
            if (start < book_end) and (book_start < end):
                return False

        self.books.add((start, end))
        return True


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class MyCalendarBinary:
    def __init__(self):
        self.head = None

    def book(self, start: int, end: int) -> bool:
        if self.head is None:
            self.head = TreeNode((start, end))
            return True

        return self.insert_node(start, end, self.head)

    def insert_node(self, start, end, current_node):
        node_start, node_end = current_node.val

        if (start < node_end) and (node_start < end):
            return False

        if (start < node_start) and (end <= node_start):
            left_child = current_node.left

            if left_child is None:
                current_node.left = TreeNode((start, end))
                return True

            return self.insert_node(start, end, left_child)

        if (node_end <= start) and (node_end < end):
            right_child = current_node.right

            if right_child is None:
                current_node.right = TreeNode((start, end))
                return True

            return self.insert_node(start, end, right_child)
