import sys

NaqeebIr = sys.stdin.readline

for Naqeeb_Irtaza_AkASH in range(int(NaqeebIr())):

    total_size = int(NaqeebIr())

    AkASH_values = list(map(int, NaqeebIr().split()))

    operation_positions = []

    Naqeeb_flip_state = 0

    for Irtaza in range(total_size - 1, -1, -1):

        current_value = AkASH_values[Irtaza]

        if Naqeeb_flip_state:
            current_value = -current_value

        if current_value > 0:
            operation_positions.append(Irtaza + 1)
            Naqeeb_flip_state ^= 1

    print(len(operation_positions))
    print(*operation_positions)