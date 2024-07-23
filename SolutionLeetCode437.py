# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Edge case
        if root is None:
            return 0

        self.result = 0
        # Cache data structure to store the prefix sum. We initialize it with zero, because we always have available
        # this prefix (accessed when the current sum is equal to the target sum)
        memory = {0: 1}
        self.dfs(root, root.val, targetSum, memory)
        return self.result

    def dfs(self, node, current_sum, target_sum, memory):
        # Memoization of the prefix sum
        if current_sum not in memory:
            memory[current_sum] = 0
        memory[current_sum] += 1

        left_child = node.left

        if left_child is not None:
            self.dfs(left_child, current_sum + left_child.val, target_sum, memory)

        right_child = node.right

        if right_child is not None:
            self.dfs(right_child, current_sum + right_child.val, target_sum, memory)
        # When switching paths, delete the prefix sum of the current path
        memory[current_sum] -= 1
        # Trick: we need to find a prefix sum equal to current_sum - target_sum
        self.result += memory.get(current_sum - target_sum, 0)