"""

abcabcbb
3

bbbbb
1

pwwkew
3
"""

def lonestSubstring(s):
  idx_of_char = {}
  mx = l = 0
  for r, char in enumerate(s):
    if char in idx_of_char and l <= idx_of_char[char]:
      l = idx_of_char[char] + 1
    else:
      mx = max(mx, r - l + 1)
    
    idx_of_char[char] = r

  return mx

print(lonestSubstring("abcabcbb"))
print(lonestSubstring("bbbbb"))
print(lonestSubstring("pwwkew"))
