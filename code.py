def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid  
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  

numbers = [2, 4, 7, 10, 13, 18, 21, 25, 30, 35]
target_value = 18

result = binary_search(numbers, target_value)


if result != -1:
    print(f"Target {target_value} found at index {result}.")
else:
    print(f"Target {target_value} not found in the list.")