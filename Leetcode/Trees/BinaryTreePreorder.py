"""
Iterative approach
Time complexity: O(n) -> We visit each node only once
Space complexity: O(n)
"""
def preorderTraversal(self, root: TreeNode) -> List[int]:
    if not root:
        return []

    result = []
    s = []
    s.append(root)

    while s:
        node = s.pop()
        result.append(node.val)

        if node.right:
            s.append(node.right)

        if node.left:
            s.append(node.left)

    return result



"""
Recursive approach
Time complexity: O(n) -> We visit each node only once
Space complexity: O(n)
"""
def preorderTraversal(self, root: TreeNode) -> List[int]:
    if not root:
        return []

    result = []

    def dfs(root):
        if root is None:
            return

        result.append(root.val)
        dfs(root.left)
        dfs(root.right)

    dfs(root)
    return result
