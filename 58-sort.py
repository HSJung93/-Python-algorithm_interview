
def quickSort(A, l, r):

  def partition(l, r):
    pivot = A[r]
    left = l
    for right in range(l, r):
      if A[right] < pivot:
        A[left], A[right] = A[right], A[left]
        left += 1
    A[left], A[r] = A[r], A[left]
    return left

  if l < r:
    pivot = partition(l, r)
    quickSort(A, l, pivot-1)
    quickSort(A, pivot+1, r)

arr = [5, 6, 3, 1, 2, 7, 10]
quickSort(arr, 0, len(arr)-1)
print(arr)

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

arr = [4, 2, 1, 3]

from typing import List

def makeLinked(arr: List[int]) -> Node:

  head = Node(arr[0])
  prev = head
  for val in arr[1:]:
    node = Node(val)
    prev.next = node
    prev = node

  return head

head = makeLinked(arr)

def merge(l1: Node, l2:Node) -> Node:
  if l1 and l2:
    if l1.val > l2.val:
      l1, l2 = l2, l1
    l1.next = merge(l1.next, l2)

  return l1 or l2

def sortList(head: Node) -> Node:
  if not (head and head.next):
    return head

  half, slow, fast = None, head, head

  while fast and fast.next:
    half, slow, fast = slow, slow.next, fast.next.next
  half.next = None

  l1 = sortList(head)
  l2 = sortList(slow)

  return merge(l1, l2)

head = sortList(head)

while head:
  print(head.val)
  head = head.next