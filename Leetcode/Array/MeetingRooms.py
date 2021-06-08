"""
Sorting Approach
Sort the intervals and compare end time of previous meeting with start time of next meeting
Time complexity: O(nlogn)
Space complexity: O(1)
"""
def canAttendMeetings(intervals: List[List[int]]) -> bool:
    intervals.sort()
    for i in range(len(intervals)-1):
        if intervals[i][1]>intervals[i+1][0]:
            return False
    return True
