def binary_search_recursive(alist, find):
    if(len(alist)==0):
        return False
    else:
        mid = len(alist)//2
        if(alist[mid]==find):
            return True
        else:
            if(alist[mid]>find):
                return binary_search_recursive(alist[:mid], find)
            else:
                return binary_search_recursive(alist[mid+1:], find)

l = [7,10,14,19,22,29,33]
print(binary_search_recursive(l,17))
