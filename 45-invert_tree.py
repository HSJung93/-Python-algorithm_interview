from collections import deque
arr = [4, 2, 7, 1, 3, 6, 9]

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

def invert_tree(root):
  if root:
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root

  return None

def invert_tree_q(root):
  q = deque([root])
  while q:
    node = q.popleft()

    if node: 
      node.left, node.right = node.right, node.left

      q.append(node.left)
      q.append(node.right)

  return root

inverted = invert_tree_q(root)

def print_tree_pre(root):
  if not root:
    return

  print(root.val)
  if root.left:
    print_tree_pre(root.left)
  if root.right:
    print_tree_pre(root.right)

print_tree_pre(inverted)


