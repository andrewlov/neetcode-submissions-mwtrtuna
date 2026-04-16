from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.hashmap = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.hashmap:
            return res
        
        timestamps = self.hashmap.get(key, [])
        
        l, r = 0, len(timestamps) - 1
        while l <= r:
            mid = (l + r) // 2
            if timestamp >= timestamps[mid][1]:
                res = timestamps[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res
        
