def read_input(filename):
    with open(filename) as f:
        arr = f.readlines()
        arr = [int(x) for x in arr]
    return arr


def merge_and_count_split_inversions(left, right):
    left_remains = len(left)
    right_remains = len(right)
    split_inversions = 0

    left_idx = 0
    right_idx = 0

    output = []

    for k in range(len(left) + len(right)):
        if left_remains == 0:
            output.extend(right[right_idx:])
            break
        elif right_remains == 0:
            output.extend(left[left_idx:])
            break

        if left[left_idx] < right[right_idx]:
            output.append(left[left_idx])
            left_idx = left_idx + 1
            left_remains = left_remains - 1
        else:
            output.append(right[right_idx])
            right_idx = right_idx + 1
            right_remains = right_remains - 1

            if left_remains > 0:
                split_inversions = split_inversions + left_remains

    return output, split_inversions


def sort_and_count(arr):
    """ Return sorted_array, inversions_in_array """
    if len(arr) == 1:
        return arr, 0
    else:
        split_pos = int(len(arr) / 2)
        left = arr[:split_pos]
        right = arr[split_pos:]

        sorted_left, left_inv = sort_and_count(left)
        sorted_right, right_inv = sort_and_count(right)
        sorted_arr, split_inv = merge_and_count_split_inversions(sorted_left, sorted_right)

        inversions = left_inv + right_inv + split_inv
        return sorted_arr, inversions


if __name__ == "__main__":
    int_arr = read_input("IntegerArray.txt")
    sorted_input, inversions = sort_and_count(int_arr)
    print(sorted_input)
    print(inversions)
