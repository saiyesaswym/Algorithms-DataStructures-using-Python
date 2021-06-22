"""
Time complexity: O(n) - visiting each node once
Space complexity: O(logn) - For recursive stack
"""
def minDepth(self, root: TreeNode) -> int:
    if not root:
        return 0

    min_depth=[]

    def helper(node,count):
        count+=1

        if node.left is None and node.right is None:
            min_depth.append(count)

        if node.left is not None:
            helper(node.left,count)

        if node.right is not None:
            helper(node.right,count)

        count-=1

    helper(root,0)
    return min(min_depth)


"""
Use one variable for comparision
"""
def minDepth(self, root: TreeNode) -> int:
    if not root:
        return 0

    mindepth=[float('inf')]

    def helper(node,count):
        count+=1
        if node.left is None and node.right is None:
            mindepth[0] = min(mindepth[0], count)

        if node.left is not None:
            helper(node.left,count)

        if node.right is not None:
            helper(node.right,count)

        count-=1

    helper(root,0)
    return mindepth[0]
