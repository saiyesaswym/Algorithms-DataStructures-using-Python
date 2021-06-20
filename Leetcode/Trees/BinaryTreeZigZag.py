"""
Time complexity: O(n)
Space complexity: O(n)
"""
def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    final_result=[]
    if not root:
        return final_result
    q = []
    q.append(root)
    level=0
    while q:
        result=[]
        for i in range(len(q)):
            node = q.pop(0)
            result.append(node.val)

            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        level+=1
        if level%2==0:
            final_result.append(result[::-1])
        else:
            final_result.append(result)
    return final_result
