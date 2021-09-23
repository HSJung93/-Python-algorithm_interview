class Node:
  def __init__(self, info):
    self.info = info
    self.next = None

def toLinked(arr):

  head = Node(arr[0])

  prev = head
  for info in arr[1:]:
    node = Node(info)
    prev.next = node
    prev = node

  return head

head = toLinked([3, 2, 3, 1, 4])

while head:
  print(head.info)
  head = head.next