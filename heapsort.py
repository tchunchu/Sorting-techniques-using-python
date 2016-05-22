__author__ = 'TARUNCH'
import  random
import  time
def heapify(A,i,n):
  l = i*2
  r = l+1
  if l <= n and A[i] < A[l]:
    m = l
  else:
    m = i
  if r <= n and A[m] < A[r]:
    m = r
  if i!=m:
    A[i] , A[m] = A[m] , A[i]
    heapify(A,m,n)

def build_heap(A,n):
 for i in range(n/2-1,0,-1):
   heapify(A,i,n)

def heap_sort( A,n ):
  build_heap(A,n)
  for i in range( len(A[1:]), 1, -1  ):
    A[ 1 ], A[ i ] = A[ i ], A[ 1 ]
    n = n-1
    heapify(A,1,n)


def main():

 #A = [0,67,98,75,64,35,68]

 A = random.sample(range(1,40000),39999)
 A.sort()

 n = len(A[1:])
 st = time.time()
 heap_sort(A,n)
 print("time",(time.time()-st)*1000)
 #print A

if __name__ == "__main__":

 main()
