nums = [1, 2, 3]

res = []

# 가장 기본적인 형태
# 자기보다 뒤의 밸류를 재귀에서 넣고, 자기 밸류를 넣을지 말지를 순회에서 결정하고, 이전 밸류들을 경로에 저장
def dfs(index, path):
  res.append(path)

  # index 3 되면 안 돌아가는 순회
  # 0, 1, 2
  # 1, 2 / 2
  # 2
  for i in range(index, len(nums)):
    # 1, [0] / 2, [1], / 3, [2]
    # 2, [0, 1] // 3, [0, 2] / 3, [1, 2] /
    # 3, [0, 1, 2] ///
    dfs(i+1, path + [nums[i]])

dfs(0, [])
print(res)