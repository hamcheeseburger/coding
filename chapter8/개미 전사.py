
# n = int(input())
# arr = list(map(int, input().split()))
#
# dpGraph = [0] * n
#
# for i in range(n):
#     print(i)
#     if i == 0 or i == 1:
#         dpGraph[i] = arr[i]
#         continue
#
#     dpGraph[i] = arr[i - 2]
#     for j in range(i - 2, -1, -1): # 0까지 실행
#         dpGraph[i] = max(dpGraph[i], dpGraph[j])
#
#     dpGraph[i] += arr[i]
#
# print(dpGraph[n - 1])

n = int(input())
arr = list(map(int, input().split()))

dpGraph = [0] * n
for i in range(2, n):
    dpGraph[i] = max(dpGraph[i-1], dpGraph[i-2] + arr[i]) # 현재 창고를 못터는 경우, 현재 창고를 털 수 있는 경우

print(dpGraph[n-1])

