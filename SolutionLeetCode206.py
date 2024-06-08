from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None) or (head.next is None):
            return head

        node_1 = None
        node_2 = head
        node_3 = head.next

        while node_2 is not None:
            node_2.next = node_1

            node_1 = node_2
            node_2 = node_3

            if node_2 is None:
                break

            node_3 = node_2.next

        return node_1



# 1 -> 2
# node1 = None
# node2 = 1
# node3 = 2
# 1   2
# node1 = 1
# node2 = 2
# node3 = None
# 1 <- 2
# node1 = 2
# node2 = None
