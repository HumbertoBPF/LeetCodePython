from typing import List

DECIMAL_PRECISION = 10


class Solution:
    # Time complexity: O(n^2)
    # Space complexity: O(n^2)
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        # Edge case: only point in the input
        if n == 1:
            return 1
        # Hash map storing a tuple of line parameters as keys and the points contained by this line as values
        lines = {}

        for i in range(n):
            for j in range(i + 1, n):
                p1 = points[i]
                p2 = points[j]

                a, b = self.get_line_params(p1, p2)

                if (a, b) not in lines:
                    lines[a, b] = set()

                lines[a, b].add(i)
                lines[a, b].add(j)

        max_points = 0

        for key in lines:
            nb_points = len(lines[key])
            max_points = max(max_points, nb_points)

        return max_points

    def round_float(self, val: float) -> int:
        return int(round(val, DECIMAL_PRECISION) * 10 ** DECIMAL_PRECISION)

    def get_line_params(self, p1: List[int], p2: List[int]):
        # Line equation
        # a = (y2 - y1)/(x2 - x1)
        # f(x) = y = a*(x - x1) + y1
        # We will adopt as a standard a function like a*x + b
        # Hence, we need to enforce x1 = 0 (then y1 = f(0)) in the equation above
        x1, y1 = p1
        x2, y2 = p2
        # Vertical line (parallel to the y-axis)
        if x1 == x2:
            a = float("inf")
            b = x1
        else :
            if x2 == 0:
                a = (y1 - y2) / (x1 - x2)
                b = y2
            else:
                slope = (y2 - y1) / (x2 - x1)
                # Computing f(0) = y0
                y0 = slope * (-x1) + y1
                # Replacing x1 and y1 with x0 and y0 respectively
                a = (y2 - y0) / x2
                b = y0
            # Avoiding float precision issues
            a = self.round_float(a)
        # Avoiding float precision issues
        b = self.round_float(b)

        return a, b


points = [[54,153],[1,3],[0,-72],[-3,3],[12,-22],[-60,-322],[0,-5],[-5,1],[5,5],[36,78],[3,-4],[5,0],[0,4],[-30,-197],[-5,0],[60,178],[0,0],[30,53],[24,28],[4,5],[2,-2],[-18,-147],[-24,-172],[-36,-222],[-42,-247],[2,3],[-12,-122],[-54,-297],[6,-47],[-5,3],[-48,-272],[-4,-2],[3,-2],[0,2],[48,128],[4,3],[2,4]]
solution = Solution()
print(solution.maxPoints(points))