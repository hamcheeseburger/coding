# p.110 상하좌우

import time
start_time = time.time()

x = 1
y = 1

n = input()
n = int(n)

x_move = [0, 0, -1, 1]
y_move = [1, -1, 0, 0]
move = ['R', 'L', 'U', 'D']

input_move = input().split()

for i in range(len(input_move)):
    index = move.index(input_move[i])

    x += x_move[index]
    y += y_move[index]

    if x < 1 or x > n or y < 1 or x > n:
        x -= x_move[index]
        y -= y_move[index]

print(str(x) + " " + str(y))

end_time = time.time()
print("time : " + str(end_time - start_time))