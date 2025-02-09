def mergesort(array):
    if len(array) in {0, 1}:
        return array

    mid_point_of_array = len(array) // 2
    return merge(mergesort(array[:mid_point_of_array]), mergesort(array[mid_point_of_array:]))


def merge(array1, array2):
    array1_idx, array2_idx = 0, 0
    built_array = []
    while True:
        # if one array has hit its limit for extensions then extend
        if array1_idx == len(array1):
            built_array.extend(array2[array2_idx:])
            break
        elif array2_idx == len(array2):
            built_array.extend(array1[array1_idx:])
            break

        # increment from the left
        array1_element = array1[array1_idx]
        array2_element = array2[array2_idx]
        # take the smaller element either on the left or right. once the element is taken, increment_the_pointer
        if array1_element <= array2_element:
            built_array.append(array1_element)
            array1_idx += 1
        elif array2_element < array1_element:
            built_array.append(array2_element)
            array2_idx += 1
    return built_array


print(mergesort([4, 5, 1, 3, 2]))
print(mergesort([3, 2, 4, 1, 6]))
print(mergesort([]))
