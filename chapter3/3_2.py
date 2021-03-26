# p.92 큰 수의 법칙

first_line = input()
second_line = input()

# input 값을 정수형으로 각각 받기
N, M, K = map(int, first_line.split())

numbers = list(map(int, second_line.split(" ")))
numbers = sorted(numbers)

# 아래는 처음 했던 풀이
# count = 0
# for i in range(M):
#     if i >= K and i % K == 0:
#         count += numbers[N - 2]
#     else:
#         count += numbers[N - 1]
#
# print(count)

# 총 덧셈 값
count = 0
# 제일 큰 수가 더해질 수 있는 빈도수
big = (M // K) * K
# 그 다음 큰 수가 더해질 수 있는 빈도수
another = M - big

# 값 계산
count += numbers[N - 1] * big
count += numbers[N - 2] * another

print(count)