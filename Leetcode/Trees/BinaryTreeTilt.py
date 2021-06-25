"""
Post order traversal
Time complexity: O(n)
Space complexity: O(h)
"""
def findTilt(self, root: TreeNode) -> int:
    tilt_sum=[0]

    def helper(node):
        if not node:
            return 0

        left_sum = helper(node.left)

        right_sum = helper(node.right)

        tilt_sum[0] += abs(left_sum - right_sum)

        return left_sum + right_sum + node.val

    helper(root)
    return tilt_sum[0]
