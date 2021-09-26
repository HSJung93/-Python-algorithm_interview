arr = [1, 2, 3, None, None, 4,5]

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def make_tree(arr):
  nodes = [False] * (len(arr) + 1)
  for i, val in enumerate(arr):
    if not val:
      continue
    nodes[i+1] = Node(val)
  
  for i in range(1, len(nodes)):
    if 2*i < len(nodes) and nodes[2*i]: 
      nodes[i].left = nodes[2*i]
    if 2*i+1 < len(nodes) and nodes[2*i+1]: 
      nodes[i].right = nodes[2*i+1]

  return nodes[1]

root = make_tree(arr)

from collections import deque

def make_arr(root):
  q = deque([root])
  arr = []

  while q:
    node = q.popleft()
    if node:
      q.append(node.left)
      q.append(node.right)
      arr.append(node.val)
    else:
      arr.append(None)

  return arr

print(make_arr(root))