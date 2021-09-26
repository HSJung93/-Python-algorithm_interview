class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

arr = [0, 5, 7, 9, -10, -7, -3]
arr.sort()

def make_BST(sorted):
  if not sorted:
    return None

  mid = len(sorted) // 2

  node = Node(sorted[mid])
  node.left = make_BST(sorted[:mid])
  node.right = make_BST(sorted[mid+1:])

  return node

root = make_BST(arr)

def print_tree_pre(root):
  if not root:
    return

  print(root.val)
  if root.left:
    print_tree_pre(root.left)
  if root.right:
    print_tree_pre(root.right)

print_tree_pre(root)

"""
0 -7 -10 -3 7 5 9

"""