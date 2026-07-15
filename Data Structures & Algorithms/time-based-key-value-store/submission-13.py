class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].append((value, timestamp))
        else:
            self.hashmap[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        value = ""
        if key in self.hashmap:
            left = 0
            right = len(self.hashmap[key]) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if self.hashmap[key][mid][1] <= timestamp:
                    value = self.hashmap[key][mid][0]
                    left = mid + 1
                else:
                    right = mid - 1
        return value