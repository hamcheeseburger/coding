max = 0
bus = 0
for i in range(10):
    inNum, outNum = map(int, input().split())
    bus -= inNum
    bus += outNum
    if max < bus:
        max = bus

print(max)