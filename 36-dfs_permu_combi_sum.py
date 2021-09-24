candidates = [2, 3, 6, 7]
target = 7

result = []

def dfs_combi(csum, index, path):
  if csum < 0:
    return 
  if csum == 0:
    result.append(path)
    return

  for i in range(index, len(candidates)):
    # print(f"now searching{list(range(index, len(candidates)))}")
    print(i, end ="")
    # append 해서 넣어주기 보다, 보다 직관적으로 arr를 만들어서 넣어준다. 
    dfs_combi(csum-candidates[i], i, path + [candidates[i]])
    
# 인풋으로 모든 변수를 넣는 것이 아니라, target만 사용한다.
# 위치와 arr을 동시에 넣어준다
dfs_combi(target, 0, [])
print(result)

result = []

# 조건, 탐색 조건 감소, 결과
def dfs_permu(csum, index, path):
  if csum < 0:
    return 
  if csum == 0:
    result.append(path)
    return

  for i in range(index, len(candidates)):
    print(i, end ="")
    # append 해서 넣어주기 보다, 보다 직관적으로 arr를 만들어서 넣어준다. 
    dfs_permu(csum-candidates[i], 0, path + [candidates[i]])

    
dfs_permu(target, 0, [])
print(result)

candidates = [2, 3, 5]
target = 8

result = []

def dfs_combi(csum, index, path):
  if csum < 0:
    return 
  if csum == 0:
    result.append(path)
    return

  for i in range(index, len(candidates)):
    # append 해서 넣어주기 보다, 보다 직관적으로 arr를 만들어서 넣어준다. 
    dfs_combi(csum-candidates[i], i, path + [candidates[i]])
    
# 인풋으로 모든 변수를 넣는 것이 아니라, target만 사용한다.
# 위치와 arr을 동시에 넣어준다
dfs_combi(target, 0, [])
print(result)

result = []

# 조건, 탐색 조건 감소, 결과
def dfs_permu(csum, index, path):
  if csum < 0:
    return 
  if csum == 0:
    result.append(path)
    return

  for i in range(index, len(candidates)):
    # append 해서 넣어주기 보다, 보다 직관적으로 arr를 만들어서 넣어준다. 
    dfs_permu(csum-candidates[i], 0, path + [candidates[i]])

    
dfs_permu(target, 0, [])
print(result)