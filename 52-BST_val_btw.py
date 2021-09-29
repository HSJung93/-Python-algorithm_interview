"""
트리에서 L과 R사이의 값 더하기 

"""
arr = [10, 5, 15, 3, 7, None, 18]
L = 7
R = 15

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

## DFS brute
def rangeSumBST(root: Node, L: int, R:int) -> int:
  if not root:
    return 0

  return (root.val if L <= root.val <= R else 0 ) + rangeSumBST(root.left, L, R) + rangeSumBST(root.right, L, R)

print(rangeSumBST(root, L, R))

## DFS pruning

def rangeSumBST(root: Node, L: int, R:int) -> int:

  def dfs(node: Node):
    if not node:
      return 0

    # 현 노드의 val이 L 보다 작으면 left는 재귀적으로 찾을 필요가 없다. 이진 탐색 트리이기 때문!
    if node.val < L:
      return dfs(node.right)
    elif node.val > R:
      return dfs(node.left)

    # 현 노드의 val 이 L과 R의 사이에 있다. 
    return node.val + dfs(node.left) + dfs(node.right)

  # helper 함수를 내부적으로 정의하고 리턴하는 방식. 
  return dfs(root)

print(rangeSumBST(root, L, R))

def rangeSumBST(node: Node, L: int, R:int) -> int:

  if not node:
    return 0

    # 현 노드의 val이 L 보다 작으면 left는 재귀적으로 찾을 필요가 없다. 이진 탐색 트리이기 때문!
  if node.val < L:
    return rangeSumBST(node.right, L, R)
  elif node.val > R:
    return rangeSumBST(node.left, L, R)

    # 현 노드의 val 이 L과 R의 사이에 있다. 
  return node.val + rangeSumBST(node.left, L, R) + rangeSumBST(node.right, L, R)

  # helper 함수를 내부적으로 정의하고 리턴하는 방식. 
  return dfs(root)

print(rangeSumBST(root, L, R))

## DFS iter

def rangeSumBST(node: Node, L: int, R:int) -> int:

  stack, sum = [root], 0

  while stack:
    node = stack.pop()
    if node:
      if node.val > L:
        stack.append(node.left)
      if node.val < R:
        stack.append(node.right)
      if L <= node.val <= R:
        sum += node.val

  return sum

print(rangeSumBST(root, L, R))
