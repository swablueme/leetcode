def quickSort(array):
    def sort(array, start_idx, end_idx):
        array_without_pivot = array[start_idx: end_idx]

        # this range is end_idx - start_idx <= 0 - also known as if the array is length 1 or not
        if len(array_without_pivot) <= 0:
            return array
        to_swap_to_location_idx = start_idx

        pivot_idx = end_idx
        pivot_value = array[pivot_idx]

        for idx, current_evaluated_idx in enumerate(array_without_pivot):
            current_evaluated_idx = idx + start_idx
            value = array[current_evaluated_idx]
            if value <= pivot_value:
                swap(array, current_evaluated_idx,
                     to_swap_to_location_idx)
                to_swap_to_location_idx += 1
        swap(array, pivot_idx, to_swap_to_location_idx)

        sort(array, start_idx, max(0, to_swap_to_location_idx - 1))
        sort(array, to_swap_to_location_idx + 1, end_idx)
    sort(array, 0, len(array) - 1)


def partition(array):
    # return array[len(array) // 2]
    return -1


def swap(array, idx_from, idx_to):
    tmp = array[idx_from]
    array[idx_from] = array[idx_to]
    array[idx_to] = tmp


array = [6, 2, 4, 1, 3]

print(quickSort(array))

array = [2, 0, 2, 1, 1, 0]
print(quickSort(array))
# print(quickSort([2, 0, 2, 1, 1, 0], 0, 5))
