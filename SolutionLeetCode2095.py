from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = self.get_length(head)
        # Edge case
        if n == 1:
            return None

        i = 0
        middle_index = n // 2

        previous_node = None
        current_node = head

        while i != middle_index:
            i += 1
            previous_node = current_node
            current_node = current_node.next

        previous_node.next = current_node.next
        current_node.next = None

        return head


    def get_length(self, head):
        length = 0
        current_node = head

        while current_node is not None:
            length += 1
            current_node = current_node.next

        return length
