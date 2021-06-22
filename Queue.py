# queue=[]
# queue.append(1)
# queue.append(2)
# print(queue)
#
# print(queue.pop(0))
# print(queue)

# from collections import deque
# q= deque()
# q.append(1)
# q.append(2)
# print(q)
# print(q.popleft())
# print(q)

from queue import Queue
q= Queue(maxsize=2)
print(q.qsize())
q.put(1)
q.put(2)
print(q.full())
print(q.get())
print(q.get())
print(q.empty())