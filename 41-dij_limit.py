edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
N = 3
K = 0
src = 0
dst = 2
"""
500

"""
import heapq
from collections import defaultdict

graph = defaultdict(list)
for u, v, w in edges:
  graph[u].append((v, w))

# 거리, 다음 장소, 카운트다운
q = [(0, src, K)]
res = -1

while q:
  # 넣는 이유, 꺼내는 것과 while로 모든 것을 돌리는 것은 다름
  w, v, k = heapq.heappop(q)

  # 도착 조건
  if v == dst:
    res = w
    break

  # 도중 종료 조건(<-> 지속 조건)
  if k >= 0:
    for dv, dw in graph[v]:
      tw = w + dw
      heapq.heappush(q, (tw, dv, k-1))

print(res)

  

