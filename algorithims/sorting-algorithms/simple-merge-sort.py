unsorted_list = [8,2,6,4,5,3,7,1]
# unsorted_list = [2,4,6,8,1,3,5,7]

def merge_sort(unsorted_list):
    list_len = len(unsorted_list)
    sorted_list = list()

    split_index = int(list_len/2)

    if list_len == 1:
        return unsorted_list

    list_one = merge_sort(unsorted_list[:split_index])
    list_two = merge_sort(unsorted_list[split_index:])

    # Merge lists.
    for num in list_one:
        for num1 in list_two:
            if num > num1:
                sorted_list.append(num1)
                list_two.remove(num1)
                break

        sorted_list.append(num)

    for num in list_two:
        sorted_list.append(num)


    return sorted_list

print(merge_sort(unsorted_list))
