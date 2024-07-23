from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge cases: linked list with zero and one nodes
        if (head is None) or (head.next is None):
            return head

        current_node = head.next.next
        # We track the last node of each sub linked list.
        # The node.next = None part detaches the node from the input linked list.
        last_even_node = head.next
        last_even_node.next = None

        last_odd_node = head
        last_odd_node.next = None
        # We cache the first node of the even linked list since we will need it to bind the lists at the end
        first_even_node = last_even_node
        # We start at the third node of the linked list (head.next.next)
        # considering the one-indexing convention of the question
        counter = 3

        while current_node is not None:
            next_node = current_node.next
            # Detaching the current node from the linked list
            current_node.next = None
            # Even node
            if counter % 2 == 0:
                last_even_node.next = current_node
                last_even_node = current_node
            # Odd node
            else:
                last_odd_node.next = current_node
                last_odd_node = current_node

            counter += 1
            current_node = next_node
        # Binding the even linked list to the odd one
        last_odd_node.next = first_even_node
        return head
