# p.118 게임 개발

# left, up, right, down
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# M : 가로 N : 세로
M, N = map(int, input().split())
rt, ct, direction = map(int, input().split())

mapp = []

for i in range(N):
    n = list(map(int, input().split()))
    mapp.append(n)


def turn_left(di):
    di -= 1
    if di == -1:
        di = 3

    return di


mapp[rt][ct] = 1

turn = 0
count = 1
while True:
    # 회전
    direction = turn_left(direction)
    turn += 1

    tu = move[direction]
    rt += tu[0]
    ct += tu[1]

    # 갈 수 있는 곳 일 때
    if mapp[rt][ct] != 1 and 0 <= rt <= N and 0 <= ct <= M:
        count += 1
        mapp[rt][ct] = 1
        turn = 0
        continue
    # 못 가는 곳일 때
    else:
        rt -= tu[0]
        ct -= tu[1]

    # 사면이 갈 수 없는 곳일 때
    if turn == 4:
        rt -= (move[direction])[0]
        ct -= (move[direction])[1]

        if mapp[rt][ct] == 1:
            break
        turn = 0

    # print(mapp)

print(count)
