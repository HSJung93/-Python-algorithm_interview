"""
nums = [1, 1, 1, 2, 2, 3, 3, 4]
k = 3

[1, 2, 3]
"""

from collections import Counter

nums = [1, 1, 1, 2, 2, 3, 3, 4]
k = 3

counter = Counter(nums)
print(counter.most_common())
print(counter.most_common()[k])
print(counter.most_common(k))
print(list(zip(*counter.most_common(k)))[0])

