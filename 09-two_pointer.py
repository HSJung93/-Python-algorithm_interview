def three_sum(nums):
  res = []
  nums.sort()

  for i in range(len(nums)-2):
    if i > 0 and nums[i] == nums[i-1]:
      continue
    
    l, r = i + 1, len(nums) - 1
    while l < r:
      sm = nums[i] + nums[l] + nums[r]
      if sm < 0:
        l += 1
      elif sm > 0:
        r -= 1
      else:
        res.append([nums[i], nums[l], nums[r]])

        # while 안에 while 쓸 때에 조건문 다시 써줘서 오류를 피한다.
        while l < r and nums[l] == nums[l+1]:
          l += 1
        while l < r and nums[r] == nums[r-1]:
          r -= 1
        l += 1
        r -= 1

  return res

nums = [-1, 0, 1, 2, -1, -4]
"""
a+b+c = 0
[ [-1, 0, 1], [-1, -1, 2] ]
"""

print(three_sum(nums))

