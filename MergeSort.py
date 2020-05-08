import numpy as np
import time

def Mergesort( A ):
    if len(A) > 1:
        middle = len(A)//2
        B = A[:middle]
        C = A[middle:]
        Mergesort(B)
        Mergesort(C)
        Merge(A, B, C)

def Merge( A, B, C ):
    i = j = k = 0
    
    while i < len(B) and j < len(C):
        if (B[i] < C[j]):
            A[k] = B[i]
            i += 1
        else:
            A[k] = C[j]
            j += 1
        k +=1
    while i < len(B):
        arr[k] = B[i]
        i+=1
        k+=1
    while j < len(C):
        arr[k] = C[j]
        j+=1
        k+=1

arr = np.random.randint(1,1000, 10000)


start = time.time()
Mergesort(arr)
now = time.time()
print( now-start, "seconds")
print(arr)



                
