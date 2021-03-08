def sequential_search(alist, find):
    pos = 0
    found = False
    while pos<len(alist) and not found:
        if(alist[pos]==find):
            found = True
        else:
            pos+=1
    return found


l = [7,10,14,19,22,29,33]
print(sequential_search(l,14))
