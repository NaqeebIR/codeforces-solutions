import sys

NaqeebIr = sys.stdin.readline


def AkASH_possible(values, groups, target):
    if target == 0:
        return True

    size = len(values)
    limit = 1 << size

    made_box = [-1] * limit
    extra_load = [-1] * limit

    made_box[0] = 0
    extra_load[0] = 0

    for mask in range(limit):
        if made_box[mask] < 0:
            continue

        current_made = made_box[mask]
        current_extra = extra_load[mask]

        for Naqeeb_Irtaza_AkASH in range(size):
            if mask & (1 << Naqeeb_Irtaza_AkASH):
                continue

            next_mask = mask | (1 << Naqeeb_Irtaza_AkASH)
            new_made = current_made
            new_extra = current_extra + values[Naqeeb_Irtaza_AkASH]

            if new_extra >= target:
                new_made += 1
                new_extra = 0

            if new_made > made_box[next_mask] or (
                new_made == made_box[next_mask] and new_extra > extra_load[next_mask]
            ):
                made_box[next_mask] = new_made
                extra_load[next_mask] = new_extra

    return made_box[limit - 1] >= groups


for _ in range(int(NaqeebIr())):
    n, k = map(int, NaqeebIr().split())

    all_numbers = list(map(int, NaqeebIr().split()))

    biggest_index = 0
    for i in range(1, n):
        if all_numbers[i] > all_numbers[biggest_index]:
            biggest_index = i

    last_value = all_numbers[biggest_index]

    remaining = []
    total_sum = 0

    for i in range(n):
        if i != biggest_index:
            remaining.append(all_numbers[i])
            total_sum += all_numbers[i]

    left = 0
    right = total_sum // k
    answer = 0

    while left <= right:
        middle = (left + right) // 2

        if AkASH_possible(remaining, k, middle):
            answer = middle
            left = middle + 1
        else:
            right = middle - 1

    print(last_value + answer)