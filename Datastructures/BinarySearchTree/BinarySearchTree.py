
class Binary_Search_Tree:

    def __init__(self, data=None):
        self.data = data
        self.leftNode = None
        self.rightNode = None

def insert_node(root, val):
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
    if root.data is None:
        return None

    curr = root

    while curr is not None:
        if val == curr.data:
            print("Found")
            return curr.data
        elif val<curr.data:
            curr = curr.leftNode
        else:
            curr = curr.rightNode
    print("Not found")
    return None

def find_min_node(root):
    if root is None:
        return None

    curr = root

    while curr.leftNode is not None:
        curr = curr.leftNode

    return curr.data

def find_max_node(root):
    if root is None:
        return None

    curr = root

    while curr.rightNode is not None:
        curr = curr.rightNode

    return curr.data

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
