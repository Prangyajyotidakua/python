def max_subarray(nums):
    if not nums:
        return 0, []

    max_sum = nums[0]  # Initialize max_sum to the first element.
    current_sum = nums[0]  # Initialize current_sum to the first element.
    start = end = 0  # Initialize start and end indices for the maximum subarray.
    current_start = 0  # Initialize the current start index.

    for i in range(1, len(nums)):
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            current_start = i
        else:
            current_sum += nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = current_start
            end = i

    return max_sum, nums[start:end + 1]

# Example usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, max_subarray = max_subarray(nums)
print("Maximum Subarray Sum:", max_sum)
print("Maximum Subarray:", max_subarray)
