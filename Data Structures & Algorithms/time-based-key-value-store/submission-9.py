class TimeMap:

    def __init__(self):
       self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].append((value, timestamp))
        else:
            self.hashmap[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hashmap:
            left = 0
            right = len(self.hashmap[key]) - 1
            value = ""
            while left <= right:
                mid = left + (right - left) // 2
                if self.hashmap[key][mid][1] <= timestamp:
                    left = mid + 1
                    value = self.hashmap[key][mid][0]
                elif self.hashmap[key][mid][1] > timestamp:
                    right = mid - 1
            return value
        else:
            return ""