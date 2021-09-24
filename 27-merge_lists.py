class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

import heapq

l145 = Node(1)
l145.next = Node(4)
l145.next.next = Node(5)
l134 = Node(1)
l134.next = Node(3)
l134.next.next = Node(4)
l26 = Node(2)
l26.next = Node(6)

lists = [l145, l134, l26]

def merge_lists(lists):
  root = result = Node(None)
  heap = []
  
  for i in range(len(lists)):
    if lists[i]:
      # val이 같은 경우에 에러가 날 수 있기 때문에 몇번재 링크드 리스트인지를 나타내는 i도 그냥 넣어준다.
      heapq.heappush(heap, (lists[i].val, i, lists[i]))
      
  while heap:
    node = heapq.heappop(heap)
    idx = node[1]
    result.next = node[2]
    
    result = result.next
    if result.next:
      heapq.heappush(heap, (result.next.val, idx, result.next))
      
  # 주어진 노드로 처음 노드를 만들면 일관성이 깨지기 때문에, 빈 root 노드를 만들고 연결한 뒤, root.next를 리턴한다.
  return root.next

merged = merge_lists(lists)

while merged:
  print(merged.val)
  merged = merged.next