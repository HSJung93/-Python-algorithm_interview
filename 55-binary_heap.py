class BinaryHeap(object):
  def __init__(self):
    self.items = [None]

  def __len__(self):
    return len(self.items) - 1

  def _percolate_up(self):
    i = len(self)
    parent = i//2
    while parent >0 :
      if self.items[i] < self.times[parent]:
        self.items[parent], self.items[i] = self.items[i], self.items[parent]
      i = parent
      parent = i // 2

  def insert(self, k):
    self.items.append(k)
    self._percolate_up()

  def _percolate_down(self, idx):
    left, right = idx * 2, idx * 2 + 1
    smallest = idx

    if left <= len(self) and self.items[left] < self.items[smallest]:
      smallest = left

    if right <= len(self) and self.items[right] < self.items[smallest]:
      smallest = right

    if smallest != idx:
      self.items[idx], self.items[smallest] = self.items[smallest], self.items[idx]
      self._percolate_down(smallest)

  def extract(self):
    extracted = self.items[1]
    self.items[1] = self.items[len(self)]
    self.items.pop()
    self._percolate_down(1)
    return extracted

"""
kth 큰 요소 추출

input:
[3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4

output:
4
"""
from typing import List
import heapq

def findKthLargest(nums: List[int], k: int) -> int:
  return heapq.nlargest(k, nums)[-1]

print(findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))