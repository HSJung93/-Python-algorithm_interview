class Node:
  def __init__(self, info):
    self.info = info
    self.next = None

a, b, c, d, e = Node(1), Node(2), Node(3), Node(4), Node(5)
a.next, b.next, c.next, d.next = b, c, d, e

def reverse_recur(head):
  def helper(node, prev):
    if not node:
      return prev

    # node.next가 다음 재귀의 node로 필요해서 저장해둠
    # 현 node가 다음 재귀에서 prev가 됨
    next, node.next = node.next, prev
    return helper(next, node)

  prev = None
  return helper(head, prev)

reversed = reverse_recur(a)

import copy

for_print = copy.deepcopy(reversed)

while for_print:
  print(for_print.info)
  for_print = for_print.next

def reverse_iter(head):
  node, prev = head, None

  while node:
    # node.next가 반복을 위해 필요해서 next에 저장해둠
    next, node.next = node.next, prev
    # 다음 iter에 prev가 node.next가 된다. 
    prev, node = node, next

  return prev

reversed_again = reverse_iter(reversed)

fp = copy.deepcopy(reversed_again)

while fp:
  print(fp.info)
  fp = fp.next