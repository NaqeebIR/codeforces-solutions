import sys

NaqeebIr = sys.stdin.readline


class AkASHSegment:
    def __init__(self, values, useful):
        self.n = len(values) - 2
        size = 4 * self.n + 10
        self.positive = [0] * size
        self.negative = [0] * size
        self.lazy = [0] * size
        self.values = values
        self.useful = useful
        self.build(1, 1, self.n)

    def build(self, node, left, right):
        if left == right:
            if self.useful[left]:
                if self.values[left] > 0:
                    self.positive[node] = 1
                else:
                    self.negative[node] = 1
            return

        mid = (left + right) // 2
        self.build(node * 2, left, mid)
        self.build(node * 2 + 1, mid + 1, right)

        self.positive[node] = self.positive[node * 2] + self.positive[node * 2 + 1]
        self.negative[node] = self.negative[node * 2] + self.negative[node * 2 + 1]

    def push(self, node):
        if self.lazy[node] == 0:
            return

        left_child = node * 2
        right_child = node * 2 + 1

        self.positive[left_child], self.negative[left_child] = self.negative[left_child], self.positive[left_child]
        self.lazy[left_child] ^= 1

        self.positive[right_child], self.negative[right_child] = self.negative[right_child], self.positive[right_child]
        self.lazy[right_child] ^= 1

        self.lazy[node] = 0

    def flip_prefix(self, node, left, right, ql, qr):
        if qr < left or right < ql:
            return

        if ql <= left and right <= qr:
            self.positive[node], self.negative[node] = self.negative[node], self.positive[node]
            self.lazy[node] ^= 1
            return

        self.push(node)

        mid = (left + right) // 2
        self.flip_prefix(node * 2, left, mid, ql, qr)
        self.flip_prefix(node * 2 + 1, mid + 1, right, ql, qr)

        self.positive[node] = self.positive[node * 2] + self.positive[node * 2 + 1]
        self.negative[node] = self.negative[node * 2] + self.negative[node * 2 + 1]

    def remove_index(self, node, left, right, idx):
        if left == right:
            self.positive[node] = 0
            self.negative[node] = 0
            self.lazy[node] = 0
            return

        self.push(node)

        mid = (left + right) // 2
        if idx <= mid:
            self.remove_index(node * 2, left, mid, idx)
        else:
            self.remove_index(node * 2 + 1, mid + 1, right, idx)

        self.positive[node] = self.positive[node * 2] + self.positive[node * 2 + 1]
        self.negative[node] = self.negative[node * 2] + self.negative[node * 2 + 1]

    def first_positive(self, node, left, right):
        if left == right:
            return left

        self.push(node)

        mid = (left + right) // 2
        if self.positive[node * 2] > 0:
            return self.first_positive(node * 2, left, mid)

        return self.first_positive(node * 2 + 1, mid + 1, right)


for Naqeeb_Irtaza_AkASH in range(int(NaqeebIr())):
    n = int(NaqeebIr())

    arr = [0] + list(map(int, NaqeebIr().split())) + [0]

    prefix_absolute = [0] * (n + 2)
    suffix_sum = [0] * (n + 3)

    for i in range(1, n + 1):
        prefix_absolute[i] = prefix_absolute[i - 1] + abs(arr[i])

    for i in range(n, 0, -1):
        suffix_sum[i] = suffix_sum[i + 1] + arr[i]

    best_sum = suffix_sum[1]
    best_index = -1

    for i in range(1, n + 1):
        if arr[i] > 0:
            current = prefix_absolute[i - 1] - arr[i] + suffix_sum[i + 1]

            if current > best_sum:
                best_sum = current
                best_index = i

    if best_index == -1:
        print(0)
        print()
        continue

    target_state = [0] * (n + 2)
    useful_position = [0] * (n + 2)

    for i in range(1, best_index):
        target_state[i] = 1 if arr[i] < 0 else 0

    target_state[best_index] = 1

    total_operations = 0

    for i in range(1, best_index + 1):
        if target_state[i] != target_state[i + 1]:
            useful_position[i] = 1
            total_operations += 1

    tree = AkASHSegment(arr, useful_position)

    answer = []

    for _ in range(total_operations):
        idx = tree.first_positive(1, 1, n)
        answer.append(idx)

        tree.remove_index(1, 1, n, idx)
        tree.flip_prefix(1, 1, n, 1, idx)

    print(len(answer))
    print(*answer)