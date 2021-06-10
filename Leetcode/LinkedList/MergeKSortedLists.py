import ListNode

"""
Brute force Approach
Traverse through all the lists and store numbers in an array
Sort and create LinkedList from the array
Time complexity: O(nlogn)
Space complexity: O(n)
"""
def mergeKLists(lists: List[ListNode]) -> ListNode:
    nodes=[]

    head = point = ListNode(0)
    for l in lists:
        while l:
            nodes.append(l.val)
            l=l.next

    for x in sorted(nodes):
        point.next = ListNode(x)
        point = point.next

    return head.next
