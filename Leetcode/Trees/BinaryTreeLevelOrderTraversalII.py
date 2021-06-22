"""
Time complexity: O(n^2)
Space complexity: O(n)
"""
def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
    final_result=[]
    if not root:
        return final_result
    q = []
    q.append(root)

    while q:
        result=[]
        for i in range(len(q)):
            node = q.pop(0)
            result.append(node.val)

            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        #This is an O(n) operation
        final_result.insert(0,result)
    return final_result


"""
Time complexity: O(n)
Space complexity: O(n)
"""
def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
    final_result=[]
    if not root:
        return final_result
    q = []
    q.append(root)

    while q:
        result=[]
        for i in range(len(q)):
            node = q.pop(0)
            result.append(node.val)

            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        final_result.append(result)
    return final_result[::-1]
