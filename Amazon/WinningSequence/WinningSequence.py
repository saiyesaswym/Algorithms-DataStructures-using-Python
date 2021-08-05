

def winningSequence(num, lowerEnd, upperEnd):
    diff = upperEnd - lowerEnd

    if num>(diff*2)+1:
        return None

    res=[]
    res.append(upperEnd-1)
    val = upperEnd
    while val>=lowerEnd and len(res)<num:
        res.append(val)
        val-=1

    rem=num-len(res)
    res2=[]
    val = upperEnd-1-rem
    res2=[i for i in range(val,upperEnd-1)]
    return res2+res
