
def maxDepth(self, root: 'Node') -> int:
    if not root:
        return 0

    maxdepth=[0]

    def helper(node, count):
        count+=1

        if not node.children:
            maxdepth[0] = max(maxdepth[0], count)

        for child in node.children:
            helper(child, count)

        count-=1

    helper(root, 0)
    return maxdepth[0]
