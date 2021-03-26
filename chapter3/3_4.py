# p.99 1이 될 때까지

# N, K = map(int, input().split())
#
# count = 0
# # 1이하라면 빠져나오기
# while N > 1:
#     # 나누어진다면 나누기부터
#     if N % K == 0:
#         N = N // K
#     #  안된다면 -1
#     else:
#         N -= 1
#
#     count += 1
#
# print(count)




# 아래는 효율적인 코드
N, K = map(int, input().split())
count = 0

while True:
    # loop를 돌 때 마다 1씩 빼는 것이 아니고
    # 나눌 수 있는 수 까지 한번에 빼버리는 것
    # 예시 test case : N = 70 , K = 13
    # loop를 5번 돌아서 13의 배수로 만드는 것이 아니고
    # loop 한 번으로 13의 배수를 만드는 것
    target = (N // K) * K
    count += (N - target)
    N = target

    # 더 이상 나눌 수 없는 경우
    if N < K:
        break

    # 실질적으로 나누는 부분
    count += 1
    N = N // K

count += (N - 1)

print(count)