"""
First approach: Using List as Queue
Time complexity: O(n)
Space complexity: O(n)
Run time: 112ms
"""

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = []

    def next(self, val: int) -> float:
        size, queue = self.size, self.queue
        queue.append(val)
        # calculate the sum of the moving window
        window_sum = sum(queue[-size:])

        return window_sum / min(len(queue), size)


size=3
obj = MovingAverage(size)
print(obj.next(1))
print(obj.next(10))
print(obj.next(3))
print(obj.next(5))
