from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        self.r_queue, self.d_queue = self.get_party_queues(senate)

        while self.queues_are_not_empty():
            self.senate_round()

        if len(self.r_queue) > 0:
            return "Radiant"

        return "Dire"

    def get_party_queues(self, senate):
        n = len(senate)

        r_queue = deque()
        d_queue = deque()

        for i in range(n):
            senator = senate[i]

            if senator == "R":
                r_queue.append(i)
                continue

            d_queue.append(i)

        return r_queue, d_queue

    def senate_round(self):
        senators_who_spoke = set()

        while (self.queues_are_not_empty() and
               (self.r_queue[0] not in senators_who_spoke) and
               (self.d_queue[0] not in senators_who_spoke)
        ):
            r_senator = self.r_queue[0]
            d_senator = self.d_queue[0]

            if r_senator < d_senator:
                senators_who_spoke.add(r_senator)
                self.radiant_turn()
            else:
                senators_who_spoke.add(d_senator)
                self.dire_turn()

        while self.queues_are_not_empty() and (self.r_queue[0] not in senators_who_spoke):
            senators_who_spoke.add(self.r_queue[0])
            self.radiant_turn()

        while self.queues_are_not_empty() and (self.d_queue[0] not in senators_who_spoke):
            senators_who_spoke.add(self.d_queue[0])
            self.dire_turn()

    def queues_are_not_empty(self):
        return (len(self.r_queue) > 0) and (len(self.d_queue) > 0)

    def radiant_turn(self):
        self.r_queue.append(self.r_queue.popleft())
        self.d_queue.popleft()

    def dire_turn(self):
        self.r_queue.popleft()
        self.d_queue.append(self.d_queue.popleft())
