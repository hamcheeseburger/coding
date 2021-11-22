def solution(ings, menu, sell):
    ings_dict = {}
    for ing in ings:
        splited = ing.split()
        ings_dict[splited[0]] = int(splited[1])

    menu_dict = {}
    for menu_ele in menu:
        splited = menu_ele.split()
        ing_val = 0
        for ing in splited[1]:
            ing_val += ings_dict[ing]
        profit = int(splited[2]) - ing_val
        menu_dict[splited[0]] = profit

    answer = 0
    for sell_ele in sell:
        splited = sell_ele.split()
        answer += menu_dict[splited[0]] * int(splited[1])

    return answer