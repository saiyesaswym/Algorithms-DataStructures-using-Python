

import math

def utilizationCheck(instances, avgutil):
    flag=0
    for i in avgutil:
        if i<25 and flag==0:
            instances = math.ceil(instances/2)
            flag=10
        elif i>60 and flag==0 and instances<=108:
            instances = instances*2
            flag=10
        else:
            if flag>0:
                flag-=1
    return instances
