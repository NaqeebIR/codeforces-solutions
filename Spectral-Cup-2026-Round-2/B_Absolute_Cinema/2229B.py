import sys

NaqeebIr = sys.stdin.readline

for Naqeeb_Irtaza_AkASH in range(int(NaqeebIr())):

    length_of_array = int(NaqeebIr())

    first_box = list(map(int, NaqeebIr().split()))
    second_box = list(map(int, NaqeebIr().split()))

    total_power = 0
    hidden_bonus = 0

    for idx in range(length_of_array):

        bigger_value = first_box[idx]
        smaller_value = second_box[idx]

        if smaller_value > bigger_value:
            bigger_value, smaller_value = smaller_value, bigger_value

        total_power += bigger_value

        if smaller_value > hidden_bonus:
            hidden_bonus = smaller_value

    print(total_power + hidden_bonus)