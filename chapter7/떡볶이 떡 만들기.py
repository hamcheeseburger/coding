def makeTteok(start, end, targetLength, tteokArray):
    mid = (start + end) // 2

    restOfTteok = 0
    for tteok in tteokArray:
        if tteok - mid > 0:
            restOfTteok += (tteok - mid)

    if restOfTteok == targetLength:
        return mid
    elif restOfTteok < targetLength:
        return makeTteok(start, mid - 1, targetLength, tteokArray)
    else:
        return makeTteok(mid + 1, end, targetLength, tteokArray)


n, targetLength = list(map(int, input().split()))
tteokArray = list(map(int, input().split()))

print(makeTteok(0, max(tteokArray), targetLength, tteokArray))