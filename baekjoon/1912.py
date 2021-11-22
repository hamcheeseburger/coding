size = int(input())
num_list = list(map(int, input().split()))

max_val = 0
sum_num = 0
for num in num_list:
    sum_num += num
    if sum_num < 0:
        sum_num = 0
    if max_val < sum_num:
        max_val = sum_num

if max_val == 0:
    max_val = max(num_list)
print(max_val)