from collections import defaultdict

def check_cycle(numCourses, prerequisites):
  graph = defaultdict(list)

  for x, y in prerequisites:
    graph[x].append(y)

  traced = set()
  visited = set()

  def dfs(i):
    if i in traced:
      return False

    if i in visited:
      return True
    
    # 현 노드를 traced에 넣고 인접된 노드에 대해서 돌아오는지 확인한다.
    traced.add(i)
    for j in graph[i]:
      if not dfs(j):
        return False
    # 현 노드의 인접 노드 + 인접 노드의 인접 ...(재귀) 까지도 확인이 끝났는데, 순환하지 않음.
    # i가 순환 없이 끝에 도달 했으면 현 재귀 탐색은 True를 리턴하면서 끝이 날 것임. 그런데 다른 인접 노드의 순회의 재귀 탐색에 대해서는 모르고, 그것에 영향을 주면 안된다. 그래서 traced를 다시 제거해줘야함.
    traced.remove(i)

    # traced 작업을 끝마친 노드임
    visited.add(i)

    return True

  # key 들의 list에 대해서 반복
  for x in list(graph):
    if not dfs(x):
      return False

  return True

numCourses = 2
prerequisites = [[1, 0]]

print(check_cycle(numCourses, prerequisites))

numCourses = 2
prerequisites = [[1, 0], [0, 1]]

print(check_cycle(numCourses, prerequisites))