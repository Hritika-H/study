"""import sys
A=[int(x) for x in input().split()]
for i in range(len(A)):
    minidx=i
    for j in range(i+1,len(A)):
        if A[minidx]>A[j]:
            minidx=j
    A[i],A[minidx]=A[minidx],A[i]

print("Sorted array")
for i in range(len(A)):
    print("%d"%A[i])

print("Smallest=",A[0],"Largest=",A[len(A)-1])"""

import numpy as np
a=np.conjugate(5-4j)
print(a)
