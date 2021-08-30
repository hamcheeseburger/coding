# p.311
n = int(input())

rates = list(map(int, input().split()))

rates.sort()

print(rates)

count = 0
result = 0
for rate in rates:
    count += 1
    if count >= rate:
        result += 1
        count = 0


print(result)