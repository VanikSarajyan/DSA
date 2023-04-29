from numbers import Number


def bubble_sort(arr: list[Number]) -> list[Number]:
    for i in range(len(arr)):
        swapped = False

        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            return arr

    return arr


arr = [7, 6, 9, 0]
print(bubble_sort(arr))
