__author__ = 'TARUNCH'
import random
import time

def insertion( A ,left,right):
  for i in range( left+1, right+1,1 ):
    tmp = A[i]
    k = i
    while k > 0 and tmp < A[k - 1]:
        A[k] = A[k - 1]
        k -= 1
    A[k] = tmp
  return A


def median(A, left, right):
    center = (left + right) // 2

    if (A[center] < A[left]):
        A[center], A[left] = A[left], A[center]
    if (A[right] < A[left]):
        A[left], A[right] = A[right], A[left]
    if (A[right] < A[center]):
        A[center], A[right] = A[right], A[center]

    A[center], A[right - 1] = A[right - 1], A[center]
    return right - 1


def quicksort(A, left, right):
    if left<right:
     if left + 15 <= right:
        j = split(A, left, right)

        quicksort(A, left, j - 1)
        quicksort(A, j + 1, right)
     else:
        insertion(A,left,right,)



def split(A, left, right):
    pivot = A[median(A, left, right)]

    i = left - 1
    for k in range(left, right - 1, 1):
        if A[k] <= pivot:
            i = i + 1
            A[i], A[k] = A[k], A[i]

    A[i + 1], A[right - 1] = A[right - 1], A[i + 1]
    return i + 1




A = random.sample(range(1, 10000), 9999)
A.sort(reverse=True)
st = time.time()
quicksort(A, 0, len(A) - 1)
#print A

print("time", (time.time()-st)*1000)

