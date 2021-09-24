"""
23
["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

"""
dic = {
  "2": "abc", 
  "3": "def",
  "4": "ghi",
  "5": "jkl",
  "6": "mno",
  "7": "pqrs",
  "8": "tuv",
  "9": "wxyz"
}
result = []
digits = "23"

def dfs(index, path):
  if len(path) == len(digits):
    result.append(path)
    return

  # 재귀에 맞는 순회 구간 제한
  for i in range(index, len(digits)):
    for j in dic[digits[i]]:
      dfs(i+1, path+j)

dfs(0, "")
print(result)