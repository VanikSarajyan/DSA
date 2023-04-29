from numbers import Number


def kth_min(arr: list[Number], k: int) -> Number:
    if k > len(arr) or k <= 0:
        return None

    min_index = 0
    for i in range(len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i

    k -= 1
    min = arr.pop(min_index)

    if k == 0:
        return min
    return kth_min(arr, k)


arr = [7, 6, 3, 8, 1]
print(kth_min(arr, 3))
