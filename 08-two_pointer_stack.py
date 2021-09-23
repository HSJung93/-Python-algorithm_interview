def trap_tp(height):
  if not height:
    return 0

  volume = 0
  l, r = 0, len(height) - 1
  lm, rm = height[l], height[r]

  while l < r:
    lm, rm = max(height[l], lm), max(height[r], rm)

    # ! 더 높은 쪽을 향하여 투 포인터 이동. 결국에는 높은 쪽 기준으로 낮은 쪽의 높이 만큼 차기 때문이다.
    if lm <= rm:
      volume += lm - height[l]
      l += 1
    else:
      volume += rm - height[r]
      r -= 1

  return volume


print(trap_tp([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

def trap_st(height):

  # 스택에는 모든 점의 인덱스를 넣을 것이다.
  stack = []
  volume = 0

  for i in range(len(height)):
    
    # 상승하는 점을 찾았을 때, stack에서 상승하는 점보다 작은 모든 값을 꺼낸다. 
    while stack and height[i] > height[stack[-1]]:
      top = stack.pop()

      if not len(stack):
        break

      # 이전 높이 중에서 현재 상승하는 점의 높이 이하의 높이 점에 물을 채운다. 
      distance = i - stack[-1] - 1 # 한 칸을 차지하기 때문에 3의 거리가 2의 인덱스 차이가 되고 1이 된다. 
      waters = min(height[i], height[stack[-1]]) - height[top]

      volume += distance * waters

    stack.append(i)

  return volume


print(trap_st([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))


"""
[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

6
"""