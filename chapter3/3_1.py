# p.86 당장 좋은 것만 생각하는 그리디

# money = [500, 100, 50, 10]

# cost = input("상품금액 : ")
# payment = input("제시할 금액 : ")
#
# change = int(payment) - int(cost)
# change = 1260
# print(str(change))
#
# counter = [0 for i in range(len(money))]
# for i in range(len(money)):
#     if change <= 0:
#         break
#     count = change // money[i]
#     change -= count * money[i]
#     counter[i] = count
#
# print(money)
# print(counter)

# 아래는 정답코드
change = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    # 슬래시를 2번 하면 정수 몫이 나옴!!!!!
    count += change // coin
    change %= coin

# 최소 동전 갯수
print(count)
