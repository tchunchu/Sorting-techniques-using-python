__author__ = 'TARUNCH'
import random
import time


def mergesort(a):
    if len(a) > 1:
        mid = len(a)/2
        b = a[:mid]
        c = a[mid:]


        mergesort(b)
        mergesort(c)
        i = 0
        j = 0
        k = 0
        while i < len(b) and j < len(c):
            if b[i] < c[j]:
                a[k] = b[i]
                i = i + 1
            else:
                a[k] = c[j]
                j = j + 1
            k = k + 1

        while i < len(b):
            a[k] = b[i]
            i = i + 1
            k = k + 1
        while j < len(c):
            a[k] = c[j]
            j = j + 1
            k = k + 1

st = time.time()
a = random.sample(range(1,1000),999)
a.sort(reverse=True)
mergesort(a)
print ("%s sec" ,(time.time()-st)*1000)


