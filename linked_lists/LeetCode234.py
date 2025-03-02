from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        n = self.get_length(head)

        previous_node = None
        current_node = head
        counter = 0
        # We iterate until the middle of the linked list, and we reverse the first half in the meanwhile
        while counter < n // 2:
            next_node = current_node.next

            current_node.next = previous_node

            previous_node = current_node
            current_node = next_node
            counter += 1

        if n % 2 != 0:
            current_node = current_node.next

        symmetric_current_node = previous_node
        # Iterate over the second half while comparing to the items from the first half
        while current_node is not None:
            if current_node.val != symmetric_current_node.val:
                return False

            current_node = current_node.next
            symmetric_current_node = symmetric_current_node.next

        return True

    def get_length(self, head: ListNode):
        current_node = head
        counter = 0

        while current_node is not None:
            counter += 1
            current_node = current_node.next

        return counter
