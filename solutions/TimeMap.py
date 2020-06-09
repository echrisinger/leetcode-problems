from collections import defaultdict

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timestamp_store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamp_store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        return self._search(self.timestamp_store[key], timestamp)
    
    def _search(self, arr, val):
        left = 0
        right = len(arr)-1
        
        while right - left > 2:
            mid = left + (right - left) // 2
            if arr[mid][0] == val:
                return arr[mid][1]
            elif arr[mid][0] > val:
                right = mid - 1
            else:
                left = mid
        
        highest_ts = None
        while left <= right and arr[left][0] <= val:
            highest_ts = left
            left += 1
        
        if highest_ts is not None:
            return arr[highest_ts][1]
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# O(1), O(log n) for each operation
