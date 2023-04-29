from numbers import Number


def max_recursive(arr: list[Number]) -> Number:
    if len(arr) == 1:
        return arr[0]

    if arr[0] < max_recursive(arr[1:]):
        return max_recursive(arr[1:])
    return arr[0]


arr = [5, 6, -1, 85, 4, 10]
print(max_recursive(arr))
