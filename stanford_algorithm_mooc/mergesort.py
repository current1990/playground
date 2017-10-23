def merge(left, right):
    res = []
    idx_left = 0
    idx_right = 0

    # Merge elemtes sequentially
    while idx_left < len(left) and idx_right < len(right):
        if left[idx_left] <= right[idx_right]:
            res.append(left[idx_left])
            idx_left = idx_left + 1
        else:
            res.append(right[idx_right])
            idx_right = idx_right + 1

    # Append remaining elements
    if idx_left < len(left):
        res.extend(left[idx_left:])
    elif idx_right < len(right):
        res.extend(right[idx_right:])

    return res


def merge_sort(data):
    if len(data) < 2:
        return data
    else:
        center = len(data) / 2
        return merge(merge_sort(data[:center]), merge_sort(data[center:]))


if __name__ == "__main__":
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print merge_sort(arr)
