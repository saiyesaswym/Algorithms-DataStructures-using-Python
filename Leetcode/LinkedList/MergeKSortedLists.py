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
