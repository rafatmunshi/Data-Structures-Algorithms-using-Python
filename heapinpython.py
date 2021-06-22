from heapq import heapify, heappop, heappush

heap = []
heapify(heap)

heappush(heap, 1)
heappush(heap, 6)
heappush(heap, 0)
heappush(heap, -3)
heappush(heap, 3)

print(str(heap[0]))
print(heap)
minelement = heappop(heap)
print(str(minelement))
print(heap)
