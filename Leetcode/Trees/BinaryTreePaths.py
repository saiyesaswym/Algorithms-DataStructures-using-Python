
def binaryTreePaths(self, root: TreeNode) -> List[str]:
    final_result=[]
    if not root:
        return []

    def helper(node, slate):
        slate.append(node.val)

        if node.left is None and node.right is None:
            final_result.append("->".join(str(i) for i in slate[:]))

        if node.left is not None:
            helper(node.left, slate)

        if node.right is not None:
            helper(node.right, slate)

        slate.pop()

    helper(root, [])
    return final_result
