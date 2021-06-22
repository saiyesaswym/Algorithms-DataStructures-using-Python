"""
Time complexity: O(n) - visiting each node once
Space complexity: O(logn)
"""
def maxDepth(self, root: TreeNode) -> int:
    if not root:
        return 0

    maxdepth=[0]

    def helper(node,count):
        count+=1
        if node.left is None and node.right is None:
            maxdepth[0] = max(maxdepth[0], count)

        if node.left is not None:
            helper(node.left,count)

        if node.right is not None:
            helper(node.right,count)

        count-=1

    helper(root,0)
    return maxdepth[0]


"""
Time complexity: O(n) - visiting each node once
Space complexity: O(logn)
"""
def maxDepth(self, root: TreeNode) -> int:
    if not root:
        return 0
    else:
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return max(left_height, right_height) + 1
