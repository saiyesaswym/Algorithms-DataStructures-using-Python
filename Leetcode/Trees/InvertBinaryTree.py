"""
Time complexity: O(n)
Space complexity: O(h)
"""
def invertTree(self, root: TreeNode) -> TreeNode:
    if not root:
        return None

    def helper(node):
        if node.left is None and node.right is None:
            return

        if node.left:
            helper(node.left)

        if node.right:
            helper(node.right)

        temp = TreeNode()
        temp = node.left
        node.left = node.right
        node.right = temp

    helper(root)

    return root
