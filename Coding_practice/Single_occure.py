"""XOR"""

def find_single_occurrence(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

# Example usage:
arr = [2, 4, 3, 5, 2, 3, 4]
single_occurrence = find_single_occurrence(arr)
print(single_occurrence)  # Output: 5
