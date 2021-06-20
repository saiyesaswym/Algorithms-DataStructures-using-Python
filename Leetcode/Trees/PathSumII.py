"""
To get to a leaf --> logN
You do this N/2 times (for every leaf) -> N/2 = N
Every time you do #1, you need to add a path to the solution. Copying the path --> path is logN long
Time complexity: O(nlogn)
Space complexity: O(n)
"""
def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
    final_result=[]
    if not root:
        return []

    def helper(node, target, slate):
        slate.append(node.val)

        if node.left is None and node.right is None:
            if target==node.val:
                final_result.append(slate[:])

        if node.left is not None:
            helper(node.left, target-node.val, slate)

        if node.right is not None:
            helper(node.right, target-node.val, slate)

        slate.pop()

    helper(root, targetSum, [])
    return final_result
