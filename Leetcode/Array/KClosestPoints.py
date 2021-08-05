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


"""
Sort the array by (x2-0)^2 + (y2-0)^2
TIme complexity: O(nlogn)
Space complexity: O(1)
"""
def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    return sorted(points, key=lambda x:x[0]*x[0]+x[1]*x[1])[:k]
