times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
N = 4
K = 2
"""
4개의 노드에 대한 엣지와 비용이 있는 times로 k 부터 출발해 모든 노드가 신호를 받을 수 있는 시간를 출력. 불가능할 경우 -1
2
"""
# heapq is not deque
import heapq
from collections import defaultdict

graph = defaultdict(list)
dist = defaultdict(int)

for u, v, w in times:
  graph[u].append((w, v))

# 초기값 하나 정도는 heappush안해도 괜찮잖아?
q = [(0, K)]

while q:
  w, v = heapq.heappop(q)

  # 다익스트라기 때문에 대소 비교 안하고 바로 할당해도 된다.
  # dist로 visited 까지 같이 사용한다.
  if v not in dist:
    dist[v] = w
    for nw, nv in graph[v]:
      tw = nw + w
      heapq.heappush(q, (tw, nv))

  print(dist)

# 모든 경로에 다 갈수 있으면
if len(dist) == N:
  print(max(dist.values()))
else:
  print(-1)


