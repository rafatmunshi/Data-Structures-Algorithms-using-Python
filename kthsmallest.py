import heapq
from heapq import heappop

def kthsmallest(heap, k):
    heapq.heapify(heap) #O(n)
    while k>1: #O(k)
        heappop(heap) #(logn)
        k-=1
    return heap[0]

heap= [25, 46, 8, 4, 6, 32]
k= 3
print(str(kthsmallest(heap, k)))

# O(n+k.log(n))