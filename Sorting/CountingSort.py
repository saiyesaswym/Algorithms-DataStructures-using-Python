"""
Iterating through the input, counting the number of times each item occurs,
and using those counts to compute an item's index in the final, sorted array.
Time complexity: O(n+k) - k is the range of given input array
Space complexity: O(n+k) - Store output array and count array
"""
def countingSort(arr):
    k = max(arr)

    #Initialize count array
    out=[0]*(k+1)
    for i in arr:
        out[i]+=1

    #Initialize output array
    final = []
    for i,j in enumerate(out):
        final+=[i]*j

    return final
