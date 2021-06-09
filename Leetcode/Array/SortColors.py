"""
Dutch National Flag problem - One Pass solution
Time complexity: O(N)
Space complexity: O(1)
"""
def sortColors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    p0=0
    curr=0
    p2=len(nums)-1

    while curr<=p2:
        if nums[curr]==2:
            nums[curr],nums[p2]=nums[p2],nums[curr]
            p2-=1
        else:
            if nums[curr]==0:
                nums[curr],nums[p0]=nums[p0],nums[curr]
                p0+=1
            curr+=1


"""
Quicksort - Three way partitioning
1)<pivot
2)==pivot
3)>pivot
Recursively partiton only on the first and second lists
Time Complexity: O(nlogn)
Space complexity: O(1)
"""
def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    quickSortHelper(nums, 0, len(nums))

def partition(self, arr, start, end):
    randindex = random.randrange(start, end)

    arr[start],arr[randindex] = arr[randindex],arr[start]

    pivot = arr[start]
    left = start
    right = start

    for right in range(start+1,end):
        if arr[right] < pivot:
            left+=1
            arr[left],arr[right] = arr[right],arr[left]

    arr[start],arr[left] = arr[left],arr[start]

    k=left
    while k<end-1 and arr[k+1]==pivot:
        k+=1

    return left,k

def quickSortHelper(self, arr, start, end):
    if start < end:
        p1,p2 = partition(arr, start, end)

        quickSortHelper(arr, start, p1)
        quickSortHelper(arr, p2+1, end)

        return arr
