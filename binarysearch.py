def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Return -1 if target is not found in the array


# Example usage
arr = [2, 5, 7, 12, 16, 23, 38, 45, 56]
target = 23
result = binary_search(arr, target)

if result != -1:
    print(f'Target {target} found at index {result}')
else:
    print(f'Target {target} not found in the array')
