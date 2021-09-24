"""
[1, 2, 3]

[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

n = 4, k = 2

"""

import copy

res = []
# ! when and why this prev arr is needed?
prev = []

# arr를 줄여나간다.
def make_permu(arr):
  if len(arr) == 0:
    # 종료 조건에 만들어진 res를 담는다
    res.append(copy.deepcopy(prev))
    # return 안 넣어도 밑 부분 실행되지 않는다.
  
  for e in arr:
    next = copy.deepcopy(arr)
    next.remove(e)
    prev.append(e)
    make_permu(next)
    prev.pop()

make_permu([1, 2, 3])
print(res)


res = []

n = 4

# prev == arr 를 늘려나간다.
def make_combi(arr, index, k):
  if k == 0:
    # 종료 조건에 만들어진 res를 담는다
    res.append(copy.deepcopy(arr))
    return
  
  for i in range(index, n+1):
    arr.append(i)
    make_combi(arr, i+1, k-1)
    arr.pop()

make_combi([], 0, 2)
print(res)