"""
Iteration approach
Time complexity: O(n+m) -> Iterate through the two lists once
Space complexity: O(1)
"""
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    prehead = ListNode(-1)

    prev = prehead
    while l1 and l2:
        if l1.val <= l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next

    prev.next = l1 if l1 is not None else l2

    return prehead.next
