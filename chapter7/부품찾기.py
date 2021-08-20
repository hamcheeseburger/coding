def binary_search(start, end, target, elements):
    mid = (start + end) // 2

    if start > end:
        return False
    if elements[mid] == target:
        return True
    elif elements[mid] > target:
        return binary_search(start, mid - 1, target, elements)
    else:
        return binary_search(mid + 1, end, target, elements)


totalCount = int(input())
totalArray = list(map(int, input().split()))
totalArray = sorted(totalArray)

findCount = int(input())
findArray = list(map(int, input().split()))

answer = []
for target in findArray:
    result = binary_search(0, totalCount, target, totalArray)
    answer.append(result)

print(answer)