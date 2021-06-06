"""
Sort the array by second element - No of units in each box
Sum up until it meets the max truckSize
Time complexity: O(nlogn)
"""
def maximumUnits(boxTypes: List[List[int]], truckSize: int) -> int:
    out=0
    boxes=0
    for i in sorted(boxTypes, key=lambda x:x[1], reverse=True):
        out += i[0]*i[1]
        boxes += i[0]
        if boxes>truckSize:
            out = out - i[1]*(boxes-truckSize)
            return out
    return out
