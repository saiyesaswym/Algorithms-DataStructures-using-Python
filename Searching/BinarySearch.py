def binary_search(alist, find):
    first=0
    last=len(alist)-1
    found=False
    while first<=last and not found:
        mid=(first+last)//2
        if(alist[mid]==find):
            found=True
        else:
            if(alist[mid]>find):
                last=mid-1
            else:
                first=mid+1
    return found

l = [7,10,14,19,22,29,33]
print(binary_search(l,14))
