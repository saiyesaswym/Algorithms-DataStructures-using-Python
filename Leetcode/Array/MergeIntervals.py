"""
Sort and compare
Time complexity: O(nlogn)
Space complexity: O(n)
Assume: [[a,b],[c,d]] => [x,y]
"""
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    result=[]

    for interval in intervals:
        #Compare b and c
        if not result or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            #Get max value of b and d as y
            result[-1][1] = max(result[-1][1], interval[1])

    return result
