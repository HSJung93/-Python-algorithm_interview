"""
preorder = [3, 9, 20 ,15, 7]
inorder = [9, 3, 15, 20, 7]
 
3 9 20 15 7
"""

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

from typing import List

def build_tree(preorder: List[int], inorder: List[int]) -> Node:
  if inorder:
    # ! 전위 순회의 첫번째 결과는 정확히 중위 순위 결과를 왼쪽과 오른쪽으로 분할시키는 역할을 한다.
    index = inorder.index(preorder.pop(0))

    node = Node(inorder[index])
    node.left = build_tree(preorder, inorder[0:index])
    node.right = build_tree(preorder, inorder[index+1:])

    return node


preorder = [3, 9, 20 ,15, 7]
inorder = [9, 3, 15, 20, 7]

root = build_tree(preorder, inorder)

def print_tree_pre(root):
  if not root:
    return

  print(root.val)

  if root.left:
    print_tree_pre(root.left)
  if root.right:
    print_tree_pre(root.right)

print_tree_pre(root)