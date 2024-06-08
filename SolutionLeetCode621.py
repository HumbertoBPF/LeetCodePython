import heapq
from typing import List


class Solution:
    # Time complexity: O(nk log k)
    # Space complexity: O(k)
    # k is the length of the priority queue and n is the input length
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # O(k)
        task_priority_queue = self.get_task_priority_queue(tasks)
        # Dictionary storing the end of the cooling period as keys and the cooling task as values
        cooling_items = {}

        current_interval = 0
        # O(n * k)
        while len(task_priority_queue) != 0:
            is_cooling, nb_occurrences, task = task_priority_queue[0]
            nb_occurrences *= -1

            if not is_cooling:
                # O(log k)
                heapq.heappop(task_priority_queue)

                if nb_occurrences > 1:
                    updated_task_item = [1, -(nb_occurrences - 1), task]
                    cooling_items[current_interval + n] = updated_task_item
                    # O(log k)
                    heapq.heappush(task_priority_queue, updated_task_item)

            cooling_item = cooling_items.get(current_interval)

            if cooling_item is not None:
                cooling_item[0] = 0
                del cooling_items[current_interval]
                heapq.heapify(task_priority_queue)

            current_interval += 1

        return current_interval

    def get_task_priority_queue(self, tasks):
        task_frequency_map = self.get_task_frequency_map(tasks)

        priority_queue = []
        # For each task, we store if the task is cooling(binary flag), its frequency, and the associated label
        for task in task_frequency_map:
            frequency = task_frequency_map[task]
            # The frequency receives a minus sign since we use a min heap and tasks with higher frequency should be prioritized
            priority_queue.append([0, -frequency, task])

        heapq.heapify(priority_queue)

        return priority_queue

    def get_task_frequency_map(self, tasks):
        task_frequency_map = {}

        for task in tasks:
            if task_frequency_map.get(task) is None:
                task_frequency_map[task] = 0
            task_frequency_map[task] += 1

        return task_frequency_map
