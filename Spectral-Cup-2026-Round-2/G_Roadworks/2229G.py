import sys

NaqeebIr = sys.stdin.readline

AkASH_INF = 10**30


def Naqeeb_Irtaza_AkASH():
    total_city, total_days, start_house = map(int, NaqeebIr().split())

    start_house -= 1

    hospitality = list(map(int, NaqeebIr().split()))
    road_day = list(map(int, NaqeebIr().split()))

    earliest_reach = [0] * total_city
    earliest_reach[start_house] = 1

    for idx in range(start_house, total_city - 1):

        earliest_reach[idx + 1] = max(
            earliest_reach[idx] + 1,
            road_day[idx]
        )

        if idx == start_house and road_day[idx] == 1:
            earliest_reach[idx + 1] = 1

    for idx in range(start_house - 1, -1, -1):

        earliest_reach[idx] = max(
            earliest_reach[idx + 1] + 1,
            road_day[idx]
        )

        if idx == start_house - 1 and road_day[idx] == 1:
            earliest_reach[idx] = 1

    next_better = [total_city] * total_city
    previous_better = [-1] * total_city

    stack = [(total_city, AkASH_INF)]

    for idx in range(total_city - 1, -1, -1):

        while stack[-1][1] <= hospitality[idx]:
            stack.pop()

        next_better[idx] = stack[-1][0]

        stack.append((idx, hospitality[idx]))

    stack = [(-1, AkASH_INF)]

    for idx in range(total_city):

        while stack[-1][1] <= hospitality[idx]:
            stack.pop()

        previous_better[idx] = stack[-1][0]

        stack.append((idx, hospitality[idx]))

    prefix_sum = [0]

    for value in hospitality:
        prefix_sum.append(prefix_sum[-1] + value)

    best_path = [0] * total_city

    visiting_order = sorted(
        (earliest_reach[idx], idx)
        for idx in range(total_city)
    )

    final_answer = 0

    for _, current_house in visiting_order:

        if earliest_reach[current_house] <= total_days:

            final_answer = max(
                final_answer,
                best_path[current_house]
                + (total_days - earliest_reach[current_house] + 1)
                * hospitality[current_house]
            )

        for next_house in (
            previous_better[current_house],
            next_better[current_house]
        ):

            if next_house < 0 or next_house >= total_city:
                continue

            distance_cost = abs(next_house - current_house)

            time_gap = (
                earliest_reach[next_house]
                - earliest_reach[current_house]
            )

            if distance_cost <= time_gap:

                inside_gain = (
                    prefix_sum[max(current_house, next_house)]
                    - prefix_sum[min(current_house, next_house) + 1]
                )

                best_path[next_house] = max(
                    best_path[next_house],

                    best_path[current_house]
                    + (time_gap - distance_cost + 1)
                    * hospitality[current_house]
                    + inside_gain
                )

    print(final_answer)


test_case_count = int(NaqeebIr())

for _ in range(test_case_count):
    Naqeeb_Irtaza_AkASH()