from collections import deque
import copy

arr = [3, 9, 20, "null", "null", 15, 7]

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def make_tree(arr):
  nodes = [False] * (len(arr) + 1)
  for i, val in enumerate(arr):
    if val == "null":
      continue
    nodes[i+1] = Node(val)
  
  for i in range(1, len(nodes)):
    if 2*i < len(nodes) and nodes[2*i]: 
      nodes[i].left = nodes[2*i]
    if 2*i+1 < len(nodes) and nodes[2*i+1]: 
      nodes[i].right = nodes[2*i+1]

  return nodes[1]

root = make_tree(arr)
test = copy.deepcopy(root)

def print_tree_pre(root):
  if not root:
    return

  print(root.val)
  if root.left:
    print_tree_pre(root.left)
  if root.right:
    print_tree_pre(root.right)

print_tree_pre(test)

def depth_tree(root):
  if root is None:
    return 0

  q = deque([root])
  depth = 0

  while q:
    depth += 1
    for _ in range(len(q)):
      cur_root = q.popleft()
      if cur_root.left:
        q.append(cur_root.left)
      if cur_root.right:
        q.append(cur_root.right)

  return depth

print("depth is ")
print(depth_tree(root))