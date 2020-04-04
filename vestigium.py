import numpy as np

T = int(input())
list1=[]
list2=[]
for i in range(T):
    n=int(input())
    list1.clear()
    for x in range(n):
        list2.clear()
        list2=[int(a) for a in input().split(" ")]
        list1+=list2
    array=np.array(list1).reshape(n,n)
    trace=np.trace(array)
    r=0
    c=0
    for x in range(n):
        if len(list(array[x,:])) != len(set(array[x,:])):
            r=r+1
        if len(list(array[x,:])) != len(set(array[:,x])):
            c=c+1
    print("Case #{}: {} {} {}".format(i+1,trace,r,c))