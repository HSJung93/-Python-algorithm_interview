# global 함수 외부 값을 지속해서 바꾸고 싶을 때
# deepcopy 함수 외부 값을 유지하고 싶을 때 
arr = [1, 2, 3, 4, 5] 

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def make_tree(arr):
  nodes = [False] * (len(arr) + 1)
  for i, val in enumerate(arr):
    if not val:
      continue
    nodes[i+1] = Node(val)
  
  for i in range(1, len(nodes)):
    if 2*i < len(nodes) and nodes[2*i]: 
      nodes[i].left = nodes[2*i]
    if 2*i+1 < len(nodes) and nodes[2*i+1]: 
      nodes[i].right = nodes[2*i+1]

  return nodes[1]

root = make_tree(arr)
longest = 0
def calc(node):
  if not node:
    # -1을 리턴한다. 가장 상위의 함수에서 
    return -1

  left = calc(node.left)
  right = calc(node.right)

  # 중첩 함수에서 부모 함수의 변수를 재할당하면 참조 id 가 변경되며 별도의 로컬 변수로 선언된다. 
  # 리스트나 딕셔너리의 경우에는 메소드를 사용해 재할당 없이 조작이 가능하다.
  # 숫자나 문자인 경우 불변 객체이기 때문에 중첩함수 내에서는 값을 변경할 수 없다. 
  global longest 
  longest = max(longest, left + right + 2)
  return max(left, right) + 1

calc(root)
print(longest)

