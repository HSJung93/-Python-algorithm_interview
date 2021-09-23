class Node:
  def __init__(self, info):
    self.info = info
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

na = Node(1)
nb = Node(2)
na.next = nb

ll = LinkedList()
ll.head = na

from collections import deque

def isPalin(h):
  if not h:
    return True

  q = deque()

  node = h
  while node is not None:
    q.append(node.info)
    node = node.next

  while len(q) > 1:
    if q.popleft() != q.pop():
      return False

  return True

print(isPalin(ll.head))

nc = Node(2)
nb.next = nc
nd = Node(1)
nc.next = nd

print(isPalin(ll.head))
