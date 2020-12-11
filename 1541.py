# 잃어버린 괄호 ----미해결------------------------
# 1541번
ㄴ

expression = input()
expression = expression.replace("(", "")
expression = expression.replace(")", "")
expression_list = expression.split("-")

ind_min, sub_sum_min, sub_sum_actual_min = 0, 0, 0
for i in range(len(expression_list)):
    plus_count = expression_list[i].count("+")
    if plus_count == 0:
        if i == 0:
            s = int(expression_list[i])
            sub_sum_actual = s
        else:
            s = -int(expression_list[i])
            sub_sum_actual = -s

        if s < sub_sum_min:
            sub_sum_min = s
            ind_min = i
        elif s == sub_sum_min:
            if sub_sum_actual < sub_sum_actual_min:
                sub_sum_min = s
                ind_min = i

    else:
        expression_list_split = list(map(int, expression_list[i].split("+")))
        if i == 0:
            s = sum(expression_list_split)
            sub_sum_actual = s
        else:
            s = -sum(expression_list_split)
            sub_sum_actual = 0
            for j in range(len(expression_list_split)):
                if j == 0:
                    sub_sum_actual -= expression_list_split[j]
                else:
                    sub_sum_actual += expression_list_split[j]

        if s < sub_sum_min:
            sub_sum_min = s
            ind_min = i
        elif s == sub_sum_min:
            if sub_sum_actual < sub_sum_actual_min:
                sub_sum_min = s
                ind_min = i


total = 0
for i in range(len(expression_list)):
    plus_count = expression_list[i].count("+")
    if i == 0:
        if plus_count == 0:
            total += int(expression_list[i])
        else:
            expression_list_split = list(
                map(int, expression_list[i].split("+")))
            total += int(sum(expression_list_split))

    elif i == ind_min:
        if plus_count == 0:
            total -= int(expression_list[i])
        else:
            expression_list_split = list(
                map(int, expression_list[i].split("+")))
            total -= sum(expression_list_split)
    else:
        if plus_count == 0:
            total -= int(expression_list[i])
        else:
            expression_list_split = list(
                map(int, expression_list[i].split("+")))
            sub_sum_actual = 0
            for j in range(len(expression_list_split)):
                if j == 0:
                    sub_sum_actual -= expression_list_split[j]
                else:
                    sub_sum_actual += expression_list_split[j]
            total += sub_sum_actual

print(total)


# 그리디 알고리즘
# Silver2, 정답렬 48.373%
