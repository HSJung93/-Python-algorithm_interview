import re
print('a'.isalnum())
print('A'.lower())
print(re.sub('[^a-z0-9]', '', "a 1 ! f * ..."))
print('1'.isdigit())

"""
babad

bab

cbbd

bb
"""


def longestPalin(string):

    if len(string) < 2 or string == string[::-1]:
        return string

    # 슬라이딩 윈도우 양옆으로 밀기
    def expand(l, r):
        while l >= 0 and r < len(string) and string[l] == string[r]:
            l -= 1
            r += 1
        # l+1==r이면 빈 문자열이 출력된다.
        return string[l+1:r]

    result = ""

    # 슬라이딩 윈도우
    for i in range(len(string)-1):
        # 짝 홀을 그냥 따로 구현해버림
        result = max(result, expand(i, i+1), expand(i, i+2), key=len)

    return result

print(longestPalin("babad"))
print(longestPalin("cbbd"))

print("asdfasdf"[2:2])