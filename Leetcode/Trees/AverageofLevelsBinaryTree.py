"""
Time complexity: O(n)
Space complexity: O(n)
"""
def averageOfLevels(self, root: TreeNode) -> List[float]:
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
        final_result.append(sum(result)/count)
    return final_result
