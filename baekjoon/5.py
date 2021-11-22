def getNext(num, size):
    if num == size - 1:
        return 0
    return num + 1


# 이부분 개선필요
def checkZero(answer):
    for line in answer:
        if 0 in line:
            return True

    return False


def solution(rows, columns):
    answer = [[0] * columns for _ in range(rows)]

    cnt = 1
    row = 0
    col = 0
    answer[0][0] = 1
    going = True

    while going:
        if cnt % 2 == 0:
            # row 값 증가
            row = getNext(row, rows)
        else:
            # col 값 증가
            col = getNext(col, columns)
        cnt += 1
        answer[row][col] = cnt

        # row, col 크기가 다른 경우, 매번 0이 남았는지 확인해야 함
        if rows != columns:
            going = checkZero(answer)
        # row, col 크기가 같은 경우, 패턴이 반복되지 않게 종료(cnt가 row, col의 두배가 되는 순간 종료)
        elif cnt == rows * 2:
            going = False

    return answer