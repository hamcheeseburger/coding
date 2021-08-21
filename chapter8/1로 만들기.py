# 탑다운 재귀 방식
# dpgraph = {}
#
#
# def makeOne(num):
#     # print(num)
#     if num == 1:
#         return 0
#
#     if dpgraph.get(num):
#         return dpgraph[num]
#
#     minArray = []
#     if num % 5 == 0:
#         minArray.append(makeOne(num // 5) + 1)
#
#     if num % 3 == 0:
#         minArray.append(makeOne(num // 3) + 1)
#
#     if num % 2 == 0:
#         minArray.append(makeOne(num // 2) + 1)
#
#     minArray.append(makeOne(num - 1) + 1)
#
#     dpgraph[num] = min(minArray)
#     return dpgraph[num]
#
#
#
# print(makeOne(int(input())))


# 바텀업 루프문 방식
target = int(input())
dpArray = [0] * (target + 1)
for n in range(2, target + 1):
    minArray = []
    minArray.append(dpArray[n-1] + 1)
    if n % 5 == 0:
        minArray.append(dpArray[n // 5] + 1)
    if n % 3 == 0:
        minArray.append(dpArray[n // 3] + 1)
    if n % 2 == 0:
        minArray.append(dpArray[n // 2] + 1)

    dpArray[n] = min(minArray)

print(dpArray[target])

