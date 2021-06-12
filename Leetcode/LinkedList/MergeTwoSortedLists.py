import ListNode

"""
Iteration approach
Time complexity: O(n+m) -> Iterate through the two lists once
Space complexity: O(n)
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



"""
Divide and Conquer approach - Merge
Merge pairs of lists contiously until one list is left
Time complexity: O(Nlogk)
Space complexity: O(1)
"""
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        total=len(lists)
        interval=1

        while interval<total:
            for i in range(0,total-interval,interval*2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i+interval])
            interval*=2

        return lists[0] if total>0 else None


    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
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
