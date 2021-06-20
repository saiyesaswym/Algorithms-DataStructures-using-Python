"""
Adding the right most node in each level
"""
def rightSideView(self, root: TreeNode) -> List[int]:
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
        final_result.append(result[-1])
    return final_result
