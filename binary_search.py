def binary_search(arr, key, start, end):
    if end >= start:
        mid = (start + end) // 2

        if key == arr[mid]:
            return mid
        if key > arr[mid]:
            return binary_search(arr, key, mid + 1, end)
        else:
            return binary_search(arr, key, start, mid - 1)
    else:
        return -1


arr = [1, 6, 8, 9, 25, 38]
print(binary_search(arr, 9, 0, len(arr) - 1))
