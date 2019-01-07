def get_input():
    step = []
    turn1 = input()
    while True:
        street = input()
        if street == 'SCHOOL':
            return step, turn1
        turn = input()
        step.append([turn, street])


def turn(turns):
    if turns == 'R':
        return 'LEFT'
    elif turns == 'L':
        return 'RIGHT'
    else:
        return


def main(step, turn1):
    final_step = 'Turn {} into your HOME.'.format(turn(turn1))
    step_list = []
    for i in step:
        str1 = 'Turn {} onto {} street.'.format(turn(i[0]), i[1])
        step_list.append(str1)
    step_list.reverse()
    step_list.append(final_step)
    return step_list


def res_print(step_list):
    for i in step_list:
        print(i)


def run():
    steps, turn1 = get_input()
    step_list = main(steps, turn1)
    res_print(step_list)


run()
