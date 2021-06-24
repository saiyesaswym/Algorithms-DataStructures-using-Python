"""
Time complexity: O(n)
Space complexity: O(n)
"""
def getLonelyNodes(self, root: TreeNode) -> List[int]:
    if not root:
        return []

    def helper(node, slate):
        if node.left:
            if node.right is None:
                slate.append(node.left.val)
            helper(node.left, slate)

        if node.right:
            if node.left is None:
                slate.append(node.right.val)
            helper(node.right, slate)

        if node.left is None and node.right is None:
            return

    arr=[]
    helper(root, arr)

    return arr
