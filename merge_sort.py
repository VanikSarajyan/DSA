from typing import Callable, Any


def merge(
    arr: list, start: int, mid: int, end: int, compare: Callable[[Any, Any], bool]
) -> None:
    temp = [None] * len(arr)
    i = start
    j = mid + 1
    k = start
    while i <= mid and j <= end:
        if compare(arr[i], arr[j]):
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1

        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= end:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(start, end + 1):
        arr[i] = temp[i]


def merge_sort(
    arr: list, start: int, end: int, compare: Callable[[Any, Any], bool]
) -> None:
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid, compare)
        merge_sort(arr, mid + 1, end, compare)
        merge(arr, start, mid, end, compare)


arr = [5, 7, 9, 0, 1, 8, -5]
merge_sort(arr, 0, len(arr) - 1, lambda x, y: x < y)
print(arr)
