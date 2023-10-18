def remove_duplicates(nums):
    if not nums:
        return 0

    unique_index = 0  # Index for the last unique element

    for i in range(1, len(nums)):
        if nums[i] != nums[unique_index]:
            unique_index += 1
            nums[unique_index] = nums[i]

    return unique_index + 1  # Length of the new array without duplicates

# Example usage:
sorted_array = [0, 0, 1, 1, 1, 2, 2, 3, 4]
new_length = remove_duplicates(sorted_array)

print("Updated Array:", sorted_array[:new_length])
print("New Length:", new_length)
