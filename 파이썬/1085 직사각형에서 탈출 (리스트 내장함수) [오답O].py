'''
x, y, w, h = map(int, input().split())

diff = 1001
if w-x < diff:
    diff = w-x
if x < diff:
    diff = x
if h-y < diff:
    diff = h-y
if y < diff:
    diff = y
print(diff)
'''

# 더 깔끔한 소스
x, y, w, h = list(map(int, input().split()))
print(min([x, y, w - x, h - y]))
