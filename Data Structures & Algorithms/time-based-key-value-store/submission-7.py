class TimeMap:

    def __init__(self):
        self.keyStore = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        vals = self.keyStore.get(key, "")
        res= ""
        l, r = 0, len(vals) - 1
        
        while l <= r:
            m = l + (r - l) // 2

            if vals[m][1] <= timestamp:
                res = vals[m][0]
                l = m + 1
            else:
                r = m -1
        return res


