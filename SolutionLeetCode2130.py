from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = self.get_size(head)

        counter = 1
        parent_node = None
        current_node = head

        while counter <= n // 2:
            parent_node = current_node
            current_node = current_node.next
            counter += 1
        # Separate the first half of the linked list from the second half
        parent_node.next = None
        # Reverse the second half of the input linked list after it is separated
        head_2 = self.reverse(current_node)

        max_pair_sum = 0

        pointer_1 = head
        pointer_2 = head_2

        for i in range(n//2):
            max_pair_sum = max(max_pair_sum, pointer_1.val + pointer_2.val)

            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.next

        return max_pair_sum

    def get_size(self, head):
        size = 1
        current_node = head

        while current_node.next is not None:
            size += 1
            current_node = current_node.next

        return size

    def reverse(self, head):
        node_1 = None
        node_2 = head
        node_3 = head.next

        while True:
            node_2.next = node_1
            node_1 = node_2
            node_2 = node_3

            if node_2 is None:
                break

            node_3 = node_3.next

        return node_1
