"""
Time complexity: O(n)
Space complexity: O(n)
"""
def levelOrder(self, root: 'Node') -> List[List[int]]:
    if not root:
        return []
    final_result=[]

    q=[]
    q.append(root)

    while q:
        result=[]
        count = len(q)
        for i in range(count):
            node = q.pop(0)
            result.append(node.val)

            for child in node.children:
                q.append(child)

        final_result.append(result)
    return final_result
