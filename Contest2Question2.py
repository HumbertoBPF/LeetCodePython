class Solution(object):
    """
    :type circles: List[List[int]]
    :rtype: int
    """
    def countLatticePoints(self, circles):
        lattice_points = {}
        for circle in circles:
            lattice_points = self.get_lattice_points(circle, lattice_points)

        return len(lattice_points)

    def get_lattice_points(self, circle, lattice_points):
        x = circle[0]
        y = circle[1]
        r = circle[2]
        # We will pick all the lattice points of the square where the circle is inscribed
        for i in range(x-r, x+r+1):
            for j in range(y-r, y+r+1):
                # Checks if the points fulfill the circumference equation
                if pow((i-x), 2) + pow((j-y), 2) <= pow(r, 2):
                    lattice_points[(i, j)] = True

        return lattice_points


o1 = Solution()
print(o1.countLatticePoints([[2,2,2],[3,4,1]]))
