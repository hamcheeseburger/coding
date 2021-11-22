def get_after(now, size):
    if now == size - 1:
        return 0
    return now + 1


def get_after(now, size):
    if now == size - 1:
        return 0
    return now + 1


def get_before(now, size):
    if now == 0:
        return size - 1
    return now - 1


def solution(s):
    answer = []
    s = list(s)
    visited = []
    size = len(s)
    now = 0
    while len(visited) < size:
        if now in visited:
            now = get_after(now, size)
            continue
        visited.append(now)
        # print(now)
        # 왼쪽 순회
        i = now
        tmp = s[now]
        count = 1
        while True:
            before = get_before(i, size)
            # print(before)
            if before in visited:
                break
            if tmp != s[before]:
                break
            i = before
            visited.append(before)
            count += 1

        # 오른쪽 순회
        before_idx = i
        i = now
        while True:
            after = get_after(i, size)
            # print(after)
            if after in visited:
                break
            if tmp != s[after]:
                break
            i = after
            visited.append(after)
            count += 1

        after_idx = i
        if before_idx != now:
            now = get_before(before_idx, size)
        elif after_idx != now:
            now = get_after(after_idx, size)
        else:
            now = get_after(after_idx, size)

        answer.append(count)
        answer.sort()
    return answer