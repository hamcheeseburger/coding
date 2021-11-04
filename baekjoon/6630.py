from itertools import combinations

size = 1
result = []
while size > 0:
    input_list = list(input().split())
    size = int(input_list[0])
    del input_list[0]

    # print(input_list)

    combi = list(combinations(input_list, 6))
    for c in combi:
        # print(c)
        result.append(' '.join(c))

    result.append('line')

for ele in result:
    if ele == 'line':
        print()
    else:
        print(ele)