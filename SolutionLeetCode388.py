class TreeNode:
    def __init__(self, val, children):
        self.val = val
        self.children = children

    def __str__(self):
        return f"{self.val} {self.children}"

    def __repr__(self):
        return f"{self.val} {self.children}"


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        input_list = input.split("\n")
        root = TreeNode("", [])
        self.generate_file_tree(0, 0, input_list, root)

        memory = {"max_len": 0, "current_len": 0}

        self.dfs(root, memory)

        max_len = memory["max_len"]
        # If max_len is zero, it means that no file has been found
        if max_len == 0:
            return 0
        # We have to remove two extra slashes (the path from DFS is like "/dir/subdir/subsubdir/file.ext/", which
        # has an extra slash at the beginning and at the end)
        return memory["max_len"] - 2

    def dfs(self, current_node, memory):
        """
        Performs DFS to find the longest path of a file
        :param current_node: node currently being visited
        :param memory: memory to cache intermediary and the final result between iterations
        """
        # The added one accounts for the slashes
        memory["current_len"] += (len(current_node.val) + 1)
        # Files have dots in their names. For them, we check if the max_len was beaten
        if "." in current_node.val:
            memory["max_len"] = max(memory["max_len"], memory["current_len"])

        children = current_node.children

        for child in children:
            self.dfs(child, memory)

        memory["current_len"] -= (len(current_node.val) + 1)

    def generate_file_tree(self, i, current_depth, input_list, parent_node):
        """
        Represents the list of directories into a tree data structure
        :param i: index of the directory currently being processed
        :param current_depth: current depth in the tree
        :param input_list: directory list
        :param parent_node: node that represents the parent directory
        :return: the next index to be processed
        """
        n = len(input_list)

        current_input = input_list[i]
        name, depth = self.get_directory_attrs(current_input)

        while (i < n) and (depth >= current_depth):
            if depth > current_depth:
                i = self.generate_file_tree(i, depth, input_list, parent_node.children[-1])
            else:
                node = TreeNode(name, [])
                parent_node.children.append(node)
                i += 1

            if i >= n:
                break

            current_input = input_list[i]
            name, depth = self.get_directory_attrs(current_input)

        return i

    def get_directory_attrs(self, val_with_slash_t):
        """
        Extracts the name and the depth of a directory from its name
        :param val_with_slash_t: directory name (with "\t" included)
        :return: name of the directory without "\t" and its depth
        """
        val_without_slash_t = val_with_slash_t.split("\t")
        name = val_without_slash_t[-1]
        # The number of "/t"s represents the depth
        return name, len(val_without_slash_t) - 1


solution = Solution()
print(solution.lengthLongestPath("a"))