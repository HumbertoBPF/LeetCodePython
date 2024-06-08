class Solution:
    def carFleet(self, target, position, speed):
        n = len(position)
        cars = []
        cars_set = set()
        nb_fleets = 0

        for i in range(n):
            car = Car(i, position[i], speed[i])
            cars.append(car)
            cars_set.add(i)

        cars.sort(reverse=True, key=lambda x: x.position)

        for i in range(n):
            car_i = cars[i]

            if car_i.index not in cars_set:
                continue

            for j in range(n):
                car_j = cars[j]

                is_fleet = self.is_fleet(car_i, car_j, target)

                if is_fleet and car_j.index in cars_set:
                    cars_set.remove(car_j.index)

            nb_fleets += 1

        return nb_fleets

    def is_fleet(self, car1, car2, target):
        car_ahead = car1
        car_behind = car2

        if car_ahead.position == car_behind.position:
            return car_ahead.speed == car_behind.speed

        if car_behind.position > car_ahead.position:
            car_ahead = car2
            car_behind = car1

        if car_ahead.speed >= car_behind.speed:
            return False

        position_diff = car_ahead.position - car_behind.position
        speed_diff = car_behind.speed - car_ahead.speed

        meeting_time = position_diff / speed_diff
        meeting_position = car_ahead.position + car_ahead.speed * meeting_time

        return meeting_position <= target

class Car:
    def __init__(self, index, position, speed):
        self.index = index
        self.position = position
        self.speed = speed

    def __str__(self):
        return f"Index: {self.index} - Position: {self.position} - Speed: {self.speed}"

    def __repr__(self):
        return f"Index: {self.index} - Position: {self.position} - Speed: {self.speed}"


target = 10
position = [0,4,2]
speed = [2,1,3]

solution = Solution()
print(solution.carFleet(target, position, speed))

