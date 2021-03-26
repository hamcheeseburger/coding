# p.96 숫자 카드 게임

import numpy as np

N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.extend(list(map(int, input().split())))

arr = np.array(arr).reshape(N, M)

n = 0
for i in range(N):
    if n < arr[i].min():
        n = arr[i].min()

print(n)

# 아래는 조금 더 효율적인 답안
# N, M = map(int, input().split())
#
# n = 0
# for i in range(N):
#     arr = list(map(int, input().split()))
#
#     if n < min(arr):
#         n = min(arr)
#
#
# print(n)