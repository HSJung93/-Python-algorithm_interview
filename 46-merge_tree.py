arr1 = [1, 3, 2, 5]
arr2 = [2, 1, 3, None, 4, None, 7]

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

root1 = make_tree(arr1)
root2 = make_tree(arr2)

def merge_tree(t1, t2):
  # 둘다 존재할 경우
  if t1 and t2:
    node = Node(t1.val + t2.val)
    node.left = merge_tree(t1.left, t2.left)
    node.right = merge_tree(t1.right, t2.right)
    # 첫 노드는 무조건 있으므로 무조건 끝남.
    return node
  # else 없어도 됨
  else:
    # 존재하는 노드를 return 한다.
    # 없으면 False
    return t1 or t2

merged = merge_tree(root1, root2)

def print_tree_pre(root):
  if not root:
    return

  print(root.val)
  if root.left:
    print_tree_pre(root.left)
  if root.right:
    print_tree_pre(root.right)

print_tree_pre(merged)