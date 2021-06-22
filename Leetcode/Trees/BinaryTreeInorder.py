
def inorderTraversal(self, root: TreeNode) -> List[int]:
    if not root:
        return []
    result = []
    s = []
    curr = root

    while s or curr:
        if curr:
            s.append(curr)
            curr = curr.left
        else:
            curr = s.pop()
            result.append(curr.val)
            curr = curr.right

    return result
