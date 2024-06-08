class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.time_map.get(key) is None:
            self.time_map[key] = []

        self.time_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.time_map.get(key)

        if values is None:
            return ""

        n = len(values)

        if n == 1:
            unique_value = values[0]
            # We have to return always timestamps lower than the target timestamp
            if unique_value[1] > timestamp:
                return ""

            return unique_value[0]

        lower_bound = 0
        upper_bound = n - 1

        value_lower_bound = values[lower_bound]
        value_upper_bound = values[upper_bound]
        # We have to return always timestamps lower than the target timestamp
        if value_lower_bound[1] > timestamp:
            return ""

        if value_lower_bound[1] == timestamp:
            return value_lower_bound[0]

        if value_upper_bound[1] <= timestamp:
            return value_upper_bound[0]
        # Timestamp is between the lower and upper bounds
        while upper_bound - lower_bound > 1:
            mid = (lower_bound + upper_bound) // 2

            value_mid = values[mid]

            if value_mid[1] == timestamp:
                return value_mid[0]

            if value_mid[1] > timestamp:
                upper_bound = mid
                continue

            lower_bound = mid

        return values[lower_bound][0]


# [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
# "love": [["high", 10], ["low", 20]]
# key = "love", timestamp = 5