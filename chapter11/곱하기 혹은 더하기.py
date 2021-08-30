string_list = list(input())
int_list = list(map(int, string_list))


def get_max_integer(int_list):

    if len(int_list) == 1:
        return int_list[0]

    previous = max(int_list[0] + int_list[1], int_list[0] * int_list[1])
    for i in range(2, len(int_list)):
        print(previous)
        previous = max(int_list[i] + previous, int_list[i] * previous)

    return previous


print(get_max_integer(int_list))
