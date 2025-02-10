def quickSort(array):
    if len(array) <= 1:
        return array
    to_swap_to_location_idx = 0
    partition_idx = partition(array)
    partition_value = array[partition_idx]

    for current_evaluated_idx, value in enumerate(array[:-1]):
        if value <= partition_value:
            swap(array, current_evaluated_idx, to_swap_to_location_idx)
            to_swap_to_location_idx += 1
    swap(array, partition_idx, to_swap_to_location_idx)

    return quickSort(array[:to_swap_to_location_idx]) + quickSort(array[to_swap_to_location_idx:])


def partition(array):
    # return array[len(array) // 2]
    return -1


def swap(array, idx_from, idx_to):
    tmp = array[idx_from]
    array[idx_from] = array[idx_to]
    array[idx_to] = tmp


array = [6, 2, 4, 1, 3]


# print(quickSort(array))
print(quickSort([2, 0, 2, 1, 1, 0]))
