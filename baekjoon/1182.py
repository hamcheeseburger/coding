from itertools import combinations


def combination(num_list, num, total):
    combi_list = map(sum, list(combinations(num_list, num)))

    count = 0
    for ele in combi_list:
        if ele == total:
            count += 1

    return count


N, total = map(int, input().split())
num_list = list(map(int, input().split()))

total_count = 0
for i in range(1, len(num_list) + 1):
    total_count += combination(num_list, i, total)

print(total_count)