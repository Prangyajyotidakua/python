def sum(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n + sum(n - 1)

total_sum = sum(20)
print("Total sum is ", total_sum)
