
def diameterOfBinaryTree(self, root: TreeNode) -> int:
    if not root:
        return 0

    max_diameter=[0]

    def helper(node):
        if node.left is None and node.right is None:
            return 0

        mydia=0
        myheight=0

        if node.left is not None:
            left_height = helper(node.left)
            myheight = left_height+1
            mydia+=left_height+1

        if node.right is not None:
            right_height = helper(node.right)
            myheight = max(myheight, right_height+1)
            mydia+=right_height+1

        max_diameter[0] = max(max_diameter[0], mydia)

        return myheight

    helper(root)
    return max_diameter[0]
