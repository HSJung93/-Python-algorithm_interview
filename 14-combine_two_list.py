class Node:
  def __init__(self, info):
    self.info = info
    self.next = None

# class LinkedList:
#   def __init__(self):
#     self.head = None

a = Node(1)
b = Node(2)
a.next = b
c = Node(4)
b.next = c

d = Node(1)
e = Node(3)
d.next = e
f = Node(4)
e.next = f

def merge_list(l1, l2):
  if (not l1) or (l2 and l1.info > l2.info):
    l1, l2 = l2, l1
  if l1:
    l1.next = merge_list(l1.next, l2)
  return l1

merged_list = merge_list(a, d)

while merged_list:
  print(merged_list.info, end='->')
  merged_list = merged_list.next
