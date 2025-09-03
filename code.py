"""Binary Search Implementation"""
def binary_search(arr, target):
    """Perform binary search on a sorted array."""
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid
        if mid_val < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

numbers = [2, 4, 7, 10, 13, 18, 21, 25, 30, 35]
TARGET = 18

RESULT = binary_search(numbers, TARGET)


if RESULT != -1:
    print(f"Target {TARGET} found at index {RESULT}.")
else:
    print(f"Target {TARGET} not found in the list.")
