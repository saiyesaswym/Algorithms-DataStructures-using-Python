"""
Find paths to node 1 and node 2 and determine common ancestor
Time complexity: O(n)
Space complexity: O(n)
"""
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    path1=[]
    path2=[]

    def find_path(root, k, slate):
        if not root:
            return False

        slate.append(root)

        if root.val==k:
            return True

        if (root.left and find_path(root.left, k, slate)) or (root.right and find_path(root.right, k, slate)):
            return True

        slate.pop()
        return False

    find_path(root, p.val, path1)
    find_path(root, q.val, path2)

    i=0
    while i<len(path1) and i<len(path2):
        if path1[i]!=path2[i]:
            break
        i+=1

    return path1[i-1]
