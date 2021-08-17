
# 공백구분으로 입력 받기
n, m = map(int, input().split())

matrix = []
for i in range(n):
    matrix.append(list(map(int, input()))) # 입력받은 문자열의 문자들 각각 int 변환, 리스트화


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if matrix[x][y] == 0:
        matrix[x][y] = 1 # 방문처리
        dfs(x-1, y) # 이것들의 반환값은 중요하지 않다
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True

    return False

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            count += 1

print(count)

# dfs 함수로 한 뭉텅이(아이스크림)을 찾는 건 맞다
# 내 풀이와 해답의 다른 점은 나는 방문 매트릭스를 따로 두었던 것, 그리고 한 뭉텅이를 찾은 후 방문하지 않았고 0의 값을 갖는 요소를 시작점으로 재지정 했다는 점이다
# 해답은 요소 하나하나를 순회하면서 해당 요소의 유효한지(0인지) 확인하고 유효하다면 재귀순회로 상하좌우 연결된 요소들을 찾아냈다
