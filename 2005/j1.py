def my_print(text):
    pass
    print(text)

def get_input():
    my_print('Number of daytime minutes?')
    daytime_use = int(input())
    my_print('Number of evening minutes?')
    evening_use = int(input())
    my_print('Number of weekend minutes?')
    weekend_use = int(input())
    return daytime_use, evening_use, weekend_use

def plan_a(daytime_use, evening_use, weekend_use):

    daytime_money = 0

    if daytime_use >= 100:
        daytime_money = (daytime_use-100) * 25
    evening_money = evening_use * 15
    weekend_money = weekend_use * 20
    totle = daytime_money + evening_money + weekend_money
    return totle

def plan_b(daytime_use, evening_use, weekend_use):
    daytime_money = 0
    if daytime_use >= 250:
        daytime_money = (daytime_use-250) * 45
    evening_money = evening_use * 35
    weekend_money = weekend_use * 25
    totle = daytime_money + evening_money + weekend_money
    return totle


def res(daytime_use, evening_use, weekend_use):
    a_money = plan_a(daytime_use, evening_use, weekend_use)
    b_money = plan_b(daytime_use, evening_use, weekend_use)
    if a_money > b_money:
        cheapest = 'Plan B is cheapest.'
    elif a_money < b_money:
        cheapest = 'Plan A is cheapest.'
    elif a_money == b_money:
        cheapest = 'Plan A and B are the same price.'
    else:
        cheapest = ''

    return a_money, b_money, cheapest

def res_print(a_money, b_money, cheapest):
    str1 = 'Plan A costs {}\nPlan B costs {}\n{}'.format(a_money, b_money, cheapest)
    print(str1)


def main():
    input1 = get_input()
    result = res(input1[0], input1[1], input1[2])
    res_print(result[0], result[1], result[2])

main()