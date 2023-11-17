# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.
# Написать точно такую же процедуру, но в декларативном стиле

def merge_two_lists_imperative(arr_a, arr_b):
    res_arr = []
    i = j = 0
    while i < len(arr_a) and j < len(arr_b):
        if arr_a[i] > arr_b[j]:
            res_arr.append(arr_a[i])
            i += 1
        else:
            res_arr.append(arr_b[j])
            j += 1
    if i < len(arr_a):
        res_arr += arr_a[i:]
    if j < len(arr_b):
        res_arr += arr_b[j:]
    return res_arr


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge_two_lists_imperative(left, right)

print(merge_sort([1, 6, 3, 8, 9, 2, 7]))