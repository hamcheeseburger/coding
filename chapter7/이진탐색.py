
def binary_search(start, end, target, elements):
    mid = (start + end) // 2

    if start > end:
        None
    if elements[mid] == target:
        return mid
    elif elements[mid] > target:
        return binary_search(start, mid - 1, target, elements)
    else:
        return binary_search(mid + 1, end, target, elements)


n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(0, n, target, array)
print(result)