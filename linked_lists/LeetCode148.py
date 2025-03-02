from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Time complexity: O(n log n)
    # Space complexity: O(1)
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = self.get_length(head)
        # Edge case (empty linked list)
        if n == 0:
            return head

        return self.sort(head, n)

    def get_length(self, head):
        current_node = head
        length = 0

        while current_node is not None:
            length += 1
            current_node = current_node.next

        return length

    def sort(self, head, n):
        if n == 1:
            return head

        previous_node = None
        current_node = head
        counter = 0

        while counter < n // 2:
            counter += 1
            previous_node = current_node
            current_node = current_node.next
        # Splitting the linked list in half
        previous_node.next = None
        # We sort the sub linked lists
        head_1 = self.sort(head, n // 2)
        head_2 = self.sort(current_node, n - n // 2)

        return self.merge(head_1, head_2)

    def merge(self, head_1, head_2):
        current_node_1 = head_1
        current_node_2 = head_2

        head = None
        tail = None

        while (current_node_1 is not None) and (current_node_2 is not None):
            # We detach and append the node with the lower value
            if current_node_1.val < current_node_2.val:
                current_node_1, tail = self.detach_and_append(current_node_1, tail)
            else:
                current_node_2, tail = self.detach_and_append(current_node_2, tail)
            # Track the head of the merged linked list
            if head is None:
                head = tail
        # Adding the remaining nodes to the merged linked list
        if current_node_1 is None:
            tail.next = current_node_2

        if current_node_2 is None:
            tail.next = current_node_1

        return head

    def detach_and_append(self, head, tail):
        # Caching the next node (it will be the new head) and detaching the head
        new_head = head.next
        head.next = None
        # If the tail is None, the detached node will be the new tail
        if tail is None:
            new_tail = head
        # Appending the detached node and making the new tail point to it
        else:
            tail.next = head
            new_tail = tail.next
        # We return the new head and tail
        return new_head, new_tail
