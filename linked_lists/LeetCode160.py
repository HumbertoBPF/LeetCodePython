from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Time complexity: O(n + m)
    # Space complexity: O(1)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        n = self.get_length(headA)
        m = self.get_length(headB)

        pointer_a = headA
        pointer_b = headB

        delta = abs(n - m)
        counter = 0
        # Starting from the same position with respect to the end of the Linked Lists
        if n > m:
            while counter < delta:
                counter += 1
                pointer_a = pointer_a.next
        else:
            while counter < delta:
                counter += 1
                pointer_b = pointer_b.next

        while (pointer_a is not None) and (pointer_b is not None):
            if pointer_a == pointer_b:
                return pointer_a

            pointer_a = pointer_a.next
            pointer_b = pointer_b.next

    def get_length(self, head: ListNode):
        current_node = head
        nb_nodes = 0

        while current_node is not None:
            nb_nodes += 1
            current_node = current_node.next

        return nb_nodes
