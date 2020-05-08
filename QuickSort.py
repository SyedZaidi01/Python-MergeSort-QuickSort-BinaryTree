import numpy as np

def Quicksort(A, l, r):
    #print("IN QS")
    if l <= r:
        s = Partition(A, l , r)

        Quicksort(A, l, s-1)
        Quicksort(A, s+1, r)

    

def Partition(A, l, r):
    p = A[l]
    i = l+l
    j = r #+ 1
    flag = True
    
    while flag:
        
        #print("IN PARTITION")
        while i<=j and A[i] <= p:
            i = i + 1
        while j>=i and A[j] >= p :
            j = j -1
        if i >=j:
            flag = False
        else:
            A[i], A[j] = A[j], A[i]
    if p>A[j]:
        A[l], A[j] = A[j], A[l]
    
    return j


#arr = np.random.randint(0, 100, 10000)
#print(arr)
#print(len(arr))

arr = [3,2,4,3,1,8,6,4,3,2,6,4,78,6]

Quicksort(arr, 0, len(arr)-1)
print(arr)
