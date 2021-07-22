"""
Brute force Approach
Find max change in pass ratio for every student
Time complexity: O(n*m) - n->classes m->extraStudents
Space complexity: O(1)
"""
def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
    while extraStudents>0:
        max_percent=0
        idx=-1
        for i,c in enumerate(classes):
            if c[0]==c[1]:
                pass
            else:
                percent1 = c[0]/c[1]
                percent2 = (c[0]+1)/(c[1]+1)
                if percent2-percent1>max_percent:
                    max_percent = percent2-percent1
                    idx=i
        extraStudents-=1
        classes[idx][0]+=1
        classes[idx][1]+=1

    maxsum=0
    for c in classes:
        maxsum+=c[0]/c[1]

    return maxsum/len(classes)



"""
Using Priority Queue - MaxHeap
Time complexity: O(mlogn)
"""
def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
    #Initialize heap
    pq=[]
    #Push change in pass ratio for every student
    for p,t in classes:
        heapq.heappush(pq, (p/t - (p+1)/(t+1), p, t))

    #For every max element add 1 and push it into the queue
    while extraStudents>0:
        _,p,t = heapq.heappop(pq)
        p+=1
        t+=1

        heapq.heappush(pq, (p/t - (p+1)/(t+1), p, t))

        extraStudents-=1

    return sum([p/t for _,p,t in pq])/len(classes)
