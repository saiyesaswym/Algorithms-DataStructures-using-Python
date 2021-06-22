
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
