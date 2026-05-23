import sys

NaqeebIr = sys.stdin.readline

def Akash_check(target, upper_line, lower_line):
    double_safe = 0
    danger_blocks = 0
    previous_type = -1

    for Naqeeb_Irtaza_AkASH in range(len(upper_line)):
        count_good = 0

        if upper_line[Naqeeb_Irtaza_AkASH] >= target:
            count_good += 1
        if lower_line[Naqeeb_Irtaza_AkASH] >= target:
            count_good += 1

        if count_good == 2:
            double_safe += 1
            previous_type = 2

        elif count_good == 0:
            if previous_type != 0:
                danger_blocks += 1
            previous_type = 0

    return double_safe > danger_blocks


test_cases = int(NaqeebIr())

for _ in range(test_cases):
    column_size = int(NaqeebIr())

    first_path = list(map(int, NaqeebIr().split()))
    second_path = list(map(int, NaqeebIr().split()))

    left_side = 1
    right_side = 2 * column_size
    final_answer = 1

    while left_side <= right_side:
        middle_value = (left_side + right_side) // 2

        if Akash_check(middle_value, first_path, second_path):
            final_answer = middle_value
            left_side = middle_value + 1
        else:
            right_side = middle_value - 1

    print(final_answer)