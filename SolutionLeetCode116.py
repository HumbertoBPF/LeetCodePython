from collections import deque


# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    """
    :type root: Node
    :rtype: Node
    """
    def connect(self, root):
        # If the tree is empty, there is nothing to do
        if root is None:
            return root
        # We use a BFS to iterate over the tree since the changes that we want to do happen in each level
        nodes_to_visit = deque()
        nodes_to_visit.append(root)
        # Variable to hold the number of nodes of the next level
        number_nodes_level = len(nodes_to_visit)

        while number_nodes_level != 0:
            # Iterate over all the nodes of the current level
            for i in range(number_nodes_level):
                current_node = nodes_to_visit.popleft()
                # While we are not at the last node of the level, make the current node to point to the following one in the deque
                if i != number_nodes_level - 1:
                    current_node.next = nodes_to_visit[0]
                # Add the children nodes to the deque
                if current_node.left is not None:
                    nodes_to_visit.append(current_node.left)

                if current_node.right is not None:
                    nodes_to_visit.append(current_node.right)
            # Update the number of nodes of the next level
            number_nodes_level = len(nodes_to_visit)

        return root
