# Написать программу на любом языке в любой парадигме для
# бинарного поиска. На вход подаётся целочисленный массив и
# число. На выходе - индекс элемента или -1, в случае если искомого
# элемента нет в массиве.


def binary_search(lst, key):
    start_element = 0
    end_element = len(lst) - 1
    while start_element <= end_element:
        middle_element = start_element + (end_element - start_element) // 2
        if lst[middle_element] == key:
            return middle_element
        elif lst[middle_element] < key:
            start_element = middle_element + 1
        else:
            end_element = middle_element - 1
    return -1

lst = [1, 3, 5, 6, 7, 10, 12, 13, 16]
find_element = 5
result = binary_search(lst, find_element)
print(f"Индекс искомого элемента {find_element} = {result}")