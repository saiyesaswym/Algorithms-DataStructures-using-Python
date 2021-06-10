import ListNode

"""
Create numbers from input linked lists
Create linked list from sum number
"""
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    n1=0
    m=1
    node=l1
    while node != None:
        n1+=m*(node.val) # access the node value
        m=m*10
        node = node.next # move on to the next node

    n2=0
    m=1
    node=l2
    while node != None:
        n2+=m*(node.val) # access the node value
        m=m*10
        node = node.next # move on to the next node

    num=n1+n2
    prev=[]
    first=ListNode(0)
    while num>0:
        node = ListNode(num%10)
        if prev:
            prev.next=node
        else:
            first=node
        prev = node
        num=num//10

    return first

"""
Concise version of above approach
"""
def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    result = ListNode(0)
    result_tail = result
    carry = 0

    while l1 or l2 or carry:
        val1  = (l1.val if l1 else 0)
        val2  = (l2.val if l2 else 0)
        carry, out = divmod(val1+val2 + carry, 10)

        result_tail.next = ListNode(out)
        result_tail = result_tail.next

        l1 = (l1.next if l1 else None)
        l2 = (l2.next if l2 else None)

    return result.next
