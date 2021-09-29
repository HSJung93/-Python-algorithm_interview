"""
이진 탐색 트리에서 노드 값 차이의 최소값

input:
arr = [4, 2, 6, 1, 3, None, None]
output:
1

input: 
arr = [10, 4, 15, 1, 8, None, None]
output:
2
"""
arr = [4, 2, 6, 1, 3, None, None]

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

import math

prev = -math.inf
res = math.inf

def calc(root: Node) -> int:

  global res
  global prev

  if root.left:
    # 제일 위 층으로 나올 필요가 없고 제일 밑 층에서 return하게 된다.
    calc(root.left)

  res = min(res, root.val - prev)
  prev = root.val

  if root.right:
    calc(root.right)

  return res

print(calc(root))

arr2 = [10, 4, 15, 1, 8, None, None]
root2 = make_tree(arr2)

def calc2(root: Node) -> int:
  prev = - math.inf
  res = math.inf

  s = []

  node = root

  while s or node:
    while node:
      s.append(node)
      node = node.left

    node = s.pop()

    res = min(res, node.val-prev)
    prev = node.val

    node = node.right

  return res

print(calc2(root2))