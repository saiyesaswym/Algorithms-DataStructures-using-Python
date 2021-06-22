"""
Time complexity: O(n)
Space complexity: O(n)
"""
def levelOrder(root: TreeNode) -> List[List[int]]:
    final_result=[]
    if not root:
        return final_result
    q = []
    q.append(root)

    while q:
        result=[]
        count=len(q)
        for i in range(count):
            node = q.pop(0)
            result.append(node.val)

            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        final_result.append(result)
    return final_result


"""
Deque is preferred over list in the cases where we need quicker append and pop operations
from both the ends of container, as deque provides an O(1) time complexity
for append and pop operations as compared to list which provides O(n) time complexity.
Time complexity: O(n)
Space complexity: O(n)
"""
from collections import deque

def levelOrder(root: TreeNode) -> List[List[int]]:
    final_result=[]
    if not root:
        return final_result
    q = deque()
    q.append(root)

    while q:
        result=[]
        count=len(q)
        for i in range(count):
            node = q.popleft()
            result.append(node.val)

            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        final_result.append(result)
    return final_result
