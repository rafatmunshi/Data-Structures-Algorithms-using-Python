# stack=[]
#
# stack.append(1)
# print(stack)
# stack.pop()
# stack.pop()
# print(stack)

# from collections import deque
#
# stack= deque()
#
# stack.append(1)
# stack.append(2)
# print(stack)
#
# stack.pop()
# stack.pop()
# stack.pop()
# print(stack)

from queue import LifoQueue
stack= LifoQueue(maxsize= 2)
print(stack.qsize())

stack.put(1)
stack.put(2)

print(stack.full())

print(stack.get())
print(stack.get())
print(stack.empty())