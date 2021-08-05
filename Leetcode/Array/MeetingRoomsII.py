"""
Sort and Using Priority queue
Compare start time of every meeting with minimum end time of meetings until that point
Time complexity: O(nlogn) - sorting ; O(nlogn) - Extract n min operations;
Space complexity: O(n) - Minheap storage
"""
import heapq

def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    intervals.sort()
    free_rooms=[]
    heapq.heappush(free_rooms, intervals[0][1])
    for i in range(1,len(intervals)):
        if free_rooms[0]<=intervals[i][0]:
            heapq.heappop(free_rooms)
        heapq.heappush(free_rooms, intervals[i][1])
    return len(free_rooms)


"""
Chronological ordering - Two pointer Approach
Store start and end timings in two arrays, iterate the arrays with two pointers
When start>=end at any point, a room has become free
Time complexity: O(nlogn) - sorting
Space complexity: O(n) - Start and end arrays
"""
def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    if not intervals:
        return 0

    used_rooms = 0

    start = sorted(i[0] for i in intervals)
    end = sorted(i[1] for i in intervals)

    i=0
    j=0

    while i<len(intervals):
        if start[i]>=end[j]:
            used_rooms-=1
            j+=1
        used_rooms+=1
        i+=1

    return used_rooms
