"""
[73, 74, 75, 71, 69, 72, 76, 73]

[1, 1, 4, 2, 1, 1, 0, 0]
"""

def higher(arr):
  answer = [0] * len(arr)
  s = []
  for i, cur in enumerate(arr):
    # 특정 조건 시에 한꺼번에 많은 일이 일어날 때
    while s and cur > arr[s[-1]]:
      last = s.pop()
      answer[last] = i - last
    s.append(i)

  return answer