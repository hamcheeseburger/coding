# p.115 왕실의 나이트

colrow = input()
row_index = int(colrow[1:]) # 1
col = colrow[:1] # a

col_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
col_index = col_list.index(col) + 1

step = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

count = 0
for s in step:
    ci = col_index
    ri = row_index

    ci += s[0]
    ri += s[1]

    if 1 <= ci <= len(step) and 1 <= ri <= len(step):
        count += 1

print(count)