"""
Time complexity: O(n)
Space complexity: O(h) -- Stack space
"""
def countUnivalSubtrees(self, root: TreeNode) -> int:
    if not root:
        return 0

    count=[0]

    def helper(node):
        #Base case
        if node.left is None and node.right is None:
            count[0]+=1
            return True

        #If a node doesn't have either left/right node
        left_val = True
        right_val = True

        #Recursive case
        if node.left is not None:
            left_val = helper(node.left) and node.val == node.left.val

        if node.right is not None:
            right_val = helper(node.right) and node.val == node.right.val

        if left_val and right_val:
            count[0]+=1
            return True

        return False

    helper(root)
    return count[0]
