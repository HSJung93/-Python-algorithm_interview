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

arr = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]

root = make_BST(arr)

"""
BST의 각 노드를 현재값보다 더 큰 값을 가진 모든 노드의 합으로 만들어라.

자신보다 같거나 큰 값을ㅊ 구하려면 자기 자신을 포함한 우측 자식 노드의 합으리 구하면 된다. 
"""