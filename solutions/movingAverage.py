from queue import SimpleQueue

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = SimpleQueue()
        self.total = 0

    def next(self, val: int) -> float:
        if self.size == 0:
            self.total -= self.queue.get()
            self.size += 1
            
        self.total += val
        self.queue.put(val)
        self.size -= 1
        return self.total / self.queue.qsize()

# O(size) space, O(n) time

