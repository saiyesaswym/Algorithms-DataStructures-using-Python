"""
Time complexity: O(n)
Space complexity: O(n)
"""
def sumOfLeftLeaves(self, root: TreeNode) -> int:
    if not root:
        return 0

    left_sum = [0]

    def helper(node):
        if node.left is None and node.right is None:
            return

        if node.left:
            print(node.left.val)
            if node.left.left is None and node.left.right is None:
                left_sum[0]+=node.left.val
            helper(node.left)

        if node.right:
            helper(node.right)

    helper(root)

    return left_sum[0]
