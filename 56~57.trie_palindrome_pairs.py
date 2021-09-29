from collections import defaultdict
from typing import List

class Node:
  def __init__(self):
    self.word = False
    # Node가 값으로 있는 dict
    self.children = defaultdict(Node)

class Trie:
  def __init__(self):
    self.root = Node()

  def insert(self, word: str) -> None:
    node = self.root
    for char in word:
      # node는 다음 loop에서 부모 노드
      # dict 붙이기
      node = node.children[char] 

    # 끝 노드의 word만 True로 
    node.word = True

  def search(self, word: str) -> bool:
    node = self.root
    for char in word:
      if char not in node.children:
        return False
      node = node.children[char]
    return node.word

  def startsWith(self, prefix:str ) -> bool:
    node = self.root
    for char in prefix:
      if char not in node.children:
        return False
      node = node.children[char]
    return True

trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))

"""
input:
["abcd", "dcba", "lis", "s", "sssll"]
output:
[[0, 1], [1, 0], [3, 2], [2, 4]]

input:
["bat", "tab", "cat"]
output:
[[0, 1], [1, 0]]

input:
["d", "cbbcd", "dcbb", "dcbc", "cbbc", "bbcd"]
output:

"""

class Node:
  def __init__(self):
    self.children = defaultdict(Node)
    # word가 끝나는 지점인가 아닌가
    self.word_id = -1
    self.palindrome_word_ids = []

class Trie:
  def __init__(self):
    self.root = Node()

  @staticmethod
  def is_palindrome(word: str) -> bool:
    return word[::] == word[::-1]

  def insert(self, index: int , word: str) -> None:
    node = self.root

    # 이미 그 자체로 palin인 값들은 root.palindrome_word_ids에 저장
    for i, char in enumerate(reversed(word)):
      if self.is_palindrome(word[0:len(word)-i]):
        node.palindrome_word_ids.append(index)

      node = node.children[char] 

    # word 끝에는 원래 word의 index를 기록한다.
    node.word_id = index

  def search(self, index:int, word: str) -> bool:
    result = []
    node = self.root

    while word:

      # 탐색 중간에 word가 끝나있고, 나머지 문자가 palin 이면 palin
      # dcbc 탐색 시에 d가 들어있는 trie 구조로 체크
      if node.word_id >= 0:
        if self.is_palindrome(word):
          result.append([index, node.word_id])

      if not word[0] in node.children:
        return result

      node = node.children[word[0]]
      word = word[1:]

    # 끝까지 탐색했는데 word_id 존재
    # bbcd + dcbb
    if node.word_id >= 0 and node.word_id != index:
      result.append([index, node.word_id])

    # 끝까지 탐색했는데 palindrome_word_ids 존재
    # d + cbbcd
    for palindrome_word_id in node.palindrome_word_ids:
      result.append([index, palindrome_word_id])

    return result

def solution(words: List[str]) -> List[List[int]]:
  trie = Trie()

  for i, word in enumerate(words):
    trie.insert(i, word)

  results = []

  for i, word in enumerate(words):
    results.extend(trie.search(i, word))

  return results

print(solution(["abcd", "dcba", "lls", "s", "sssll"]))
print(solution(["bat", "tab", "cat"]))
print(solution(["d", "cbbcd", "dcbb", "dcbc", "cbbc", "bbcd"]))
