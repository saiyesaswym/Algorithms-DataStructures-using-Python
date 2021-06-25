"""
Time complexity: O(n)
Space complexity: O(n)
"""
def isUnivalTree(self, root: TreeNode) -> bool:
    if not root:
        return False

    q = deque()
    q.append(root)
    unival=root.val

    while q:
        node = q.popleft()

        if node.val!=unival:
            return False

        if node.left:
            q.append(node.left)

        if node.right:
            q.append(node.right)

    return True
