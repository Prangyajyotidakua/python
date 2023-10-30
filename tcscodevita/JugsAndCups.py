def fill_jug(cups, jug_capacity):
    cups.sort()
    n = len(cups)
    dp = [-1] * (jug_capacity + 1)
    dp[0] = 0

    for i in range(1, jug_capacity + 1):
        for j in range(n):
            if cups[j] <= i and dp[i - cups[j]] != -1:
                dp[i] = j

    if dp[jug_capacity] == -1:
        return None, None

    selected_cups = [0] * n
    x = jug_capacity
    while x > 0:
        cup_index = dp[x]
        selected_cups[cup_index] += 1
        x -= cups[cup_index]

    return selected_cups, cups

if __name__ == "__main__":
    n = int(input())
    cups = list(map(int, input().split()))
    jug_capacity = int(input())

    selected_cups, cup_sizes = fill_jug(cups, jug_capacity)

    if selected_cups is None:
        print("None")
    else:
        frequencies = selected_cups
        selected_cup_sizes = [cup_sizes[i] for i in range(n) if frequencies[i] > 0]
        selected_frequencies = [frequencies[i] for i in range(n) if frequencies[i] > 0]
        print(" ".join(map(str, selected_cup_sizes)))
        print(" ".join(map(str, selected_frequencies)))
