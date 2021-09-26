
arr = [5, 4, 5, 1, 1, 5] 

arr = [1, 4, 5, 4, 4, 5]
"""
2 : 5-5-5 
2 : 4-4-4
"""

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
longest = 0
def calc(node):
  if not node:
    # -1을 리턴한다. 가장 상위의 함수에서 
    return 0

  l = calc(node.left)
  r = calc(node.right)

  if node.left and node.left.val == node.val:
    l += 1
  else:
    l = 0
  if node.right and node.right.val == node.val:
    r += 1
  else:
    r = 0
 
  global longest 
  longest = max(longest, l + r)
  return max(l, r)

calc(root)
print(longest)

