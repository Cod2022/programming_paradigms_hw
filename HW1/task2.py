# Задача №2
# Дан список целых чисел numbers. Необходимо написать в декларативном стиле процедуру для
# сортировки числа в списке в порядке убывания.

def sort_list_declarative(arr):
    return sorted(arr, reverse=True)

print(sort_list_declarative([5, 4, 6, 8, 3, 9, 11]))