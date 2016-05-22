__author__ = 'TARUNCH'
def quicksort(A,left,right):
    if left<right:
     j = split(A,left,right)

     quicksort(A,left,j-1)
     quicksort(A,j+1,right)


def split(A,left,right):
    pivot = left + random.randrange( right - left + 1 )

    i = left-1
    for k in range(left , right, 1):
        if A[k] <= pivot:
            i=i+1
            A[i],A[k]=A[k],A[i]
    A[i+1],A[right] = A[right],A[i+1]
    return i+1



import random
import  time

A = random.sample(range(1, 40000), 39999)
A.sort()
st = time.time()
quicksort(A,0,len(A)-1)
print ("time",(time.time()-st)*1000)
#print A


