
def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
    if root is None:
        return False

    flag=[False]

    def helper(node, target):
        if node.left is None and node.right is None:
            if node.val == target:
                flag[0]=True
            return

        if node.left is not None:
            helper(node.left, target-node.val)

        if node.right is not None:
            helper(node.right, target-node.val)

    helper(root, targetSum)
    return flag[0]
