
class Binary_Search_Tree:
    def __init__(self, data=None):
        self.data = data
        self.leftNode = None
        self.rightNode = None


def insert_node(root, val):
    """
    Given the root node and key to insert
    Traverse the tree and find the position for new node
    Insert the new node to left/right of last found node
    """
    new_node = Binary_Search_Tree(val)

    if root is None:
        return new_node

    prev = None
    curr = root

    while curr is not None:
        if val==curr.data:
            print("Node already exists")
            return
        elif val<curr.data:
            prev = curr
            curr = curr.leftNode
        else:
            prev = curr
            curr = curr.rightNode

    if val<prev.data:
        prev.leftNode = new_node
    else:
        prev.rightNode = new_node


def search_node(root, val):
    """
    Given the root node and key to find
    Traverse the left or right subtree
    by comparing elements with the given key
    """
    if root.data is None:
        return None

    curr = root

    while curr is not None:
        if val == curr.data:
            print("Found")
            return curr
        elif val<curr.data:
            curr = curr.leftNode
        else:
            curr = curr.rightNode
    print("Not found")
    return None


def find_min_node(root):
    """
    Given the root node of a tree, find the min node
    Min node is the left most node
    which doesn't have any left nodes
    """
    if root is None:
        return None

    curr = root

    while curr.leftNode is not None:
        curr = curr.leftNode

    return curr.data


def find_max_node(root):
    """
    Given the root node of a tree, find the max node
    Max node is the right most node
    which doesn't have any right nodes
    """
    if root is None:
        return None

    curr = root

    while curr.rightNode is not None:
        curr = curr.rightNode

    return curr.data


def find_successor(root, val):
    """
    Min value of subtree, if given node has right subtree
    Parent is the successor, if given node is the left child
    Right ancestor up the tree, if given node is the right child
    """
    if root is None:
        return None

    #Given value of node, find node using search_node
    node = search_node(root, val)

    #If given node has a right subtree
    if node.rightNode:
        curr = node
        while curr.leftNode is not None:
            curr = curr.leftNode
        return curr

    #Start at root and traverse until given node
    ancestor = None
    curr = root
    while curr.data != node.data:
        #Store the last left parent into ancestor
        if node.data < curr.data:
            ancestor = curr
            curr = curr.leftNode
        else:
            curr = curr.rightNode

    return ancestor.data





root = insert_node(None,15)
insert_node(root,10)
insert_node(root,25)
insert_node(root,6)
print(find_min_node(root))
print(find_max_node(root))
insert_node(root,14)
insert_node(root,20)
insert_node(root,60)
print(find_min_node(root))
print(find_max_node(root))
print(search_node(root,14))
print(search_node(root,22))

print("successor to 14:")
print(find_successor(root,14))
print("successor to 20:")
print(find_successor(root,20))
