"""
Use Minheap as Priority Queue
Time complexity: O(nlogn)
Space complexity: O(n)
"""
def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    queue=[]
    for i,j in points:
        heapq.heappush(queue, (math.sqrt(i*i + j*j), i, j))

    out=[]
    while k>0:
        _,i,j = heapq.heappop(queue)
        out.append([i,j])
        k-=1

    return out
