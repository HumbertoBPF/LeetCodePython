from collections import deque
from typing import List


class Solution:
    # Time complexity: O(n^2) (time to initialize the gene graph)
    # Space complexity: O(n)
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # Trivial case
        if startGene == endGene:
            return 0
        # Using a hash map to store the genes because it is more optimized for lookups, inserts, and deletions,
        # and because the order is not important for this problem
        gene_graph = {}

        for original_gene in bank:
            gene_graph[original_gene] = []

            for mutated_gene in bank:
                if self.is_valid_mutation(original_gene, mutated_gene):
                    gene_graph[original_gene].append(mutated_gene)
        # If the target gene is not in the bank, then it cannot be obtained through mutations of startGene
        if endGene not in gene_graph:
            return -1

        return self.bfs(startGene, endGene, gene_graph)

    def bfs(self, start_gene, end_gene, gene_graph):
        queue = deque()
        visited = set()

        queue.append((end_gene, 0))
        visited.add(end_gene)

        while len(queue) > 0:
            current_gene, nb_mutations = queue.popleft()

            if self.is_valid_mutation(current_gene, start_gene):
                return nb_mutations + 1

            for gene in gene_graph[current_gene]:
                if gene not in visited:
                    queue.append((gene, nb_mutations + 1))
                    visited.add(gene)

        return -1

    def is_valid_mutation(self, gene_1, gene_2):
        nb_diff = 0

        for i in range(8):
            if gene_1[i] != gene_2[i]:
                nb_diff += 1

            if nb_diff > 1:
                return False

        return nb_diff == 1
