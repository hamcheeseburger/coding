

def doGame(participants, a, b, round):
    round += 1

    winners = []
    for i in range(0, len(participants), 2):
        # a, b가 대진을 붙을 때
        if (participants[i] == a and participants[i+1] == b) or (participants[i] == b and participants[i+1] == a):
            return round
        # 대진 중 상대 중 a나 b가 있는 경우
        if participants[i] == a or participants[i] == b:
            winners.append(participants[i])
        elif participants[i+1] == a or participants[i+1] == b:
            winners.append(participants[i+1])
        else: # 그 외는 아무나 뽑는다
            winners.append(participants[i])

    return doGame(winners, a, b, round)


def solution(n, a, b):
    participants = [i for i in range(1, n+1)]

    return doGame(participants, a, b, 0)


print("the answer ", solution(8, 4, 7))
