"""
Sliding Window Approach
Maximum Sum of any contiguous subarray of size k
Time complexity: O(n)
"""
def maxSumSubArray(arr,k):
    l=0
    r=0
    max_sum = -9999999
    curr_sum = arr[r]

    while r<len(arr)-1:
        r+=1
        curr_sum+=arr[r]
        if r-l+1==k:
            if curr_sum>max_sum:
                max_sum=curr_sum
            curr_sum-=arr[l]
            l+=1

    return max_sum
