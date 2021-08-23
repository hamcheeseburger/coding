
# def calPrice(price):
#     print(price)
#     if price in current:
#         return 1
#
#     if price <= 0:
#         return -1
#
#     minArray = []
#     for cur in current:
#         if memory[price - cur] > 0:
#             minArray.append(memory[price - cur])
#         else:
#             val = calPrice(price - cur)
#             if val != -1:
#                 memory[price - cur] = val
#                 minArray.append(val)
#
#     if len(minArray) == 0: # 이 화폐를 구성할 방법이 없음
#         return -1
#
#     return min(minArray) + 1
#
#
# n, price = list(map(int, input().split()))
# current = []
# memory = [0] * 1000
# for i in range(n):
#     val = int(input())
#     current.append(val)
#     memory[val] = 1
#
# print("정답 : " ,calPrice(price))

n, price = list(map(int, input().split()))
current = []
memory = [10001] * (price + 1) # 화폐 가치가 10000보다 작은 자연수 이기 때문에 (화폐 단위가 1이고 화폐가치가 10000인 경우 나올 수 있는 최소값은 10000이기 때문에 그것보다 크게 책정)
for i in range(n):
    val = int(input())
    current.append(val)

memory[0] = 0 # base condition
for i in range(n):
    for j in range(current[i], price + 1):
        if memory[j-current[i]] != 10001:
            memory[j] = min(memory[j], memory[j-current[i]] + 1)

if memory[price] == 10001:
    print(-1)
else:
    print(memory[price])