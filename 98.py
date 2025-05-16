def find_smallest(arr):
    if len(arr) == 1:
        return arr[0]
    return min(arr[0], find_smallest(arr[1:]))
