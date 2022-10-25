# объявление функции
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
# данные
d = [5, 7, 3, 1, 2, 9, 8]
# вызываем функцию
print(quicksort(d))

# Это же только в одну строку

d = [4, 7, 3, 5, 1, 2, 9, 6, 8]
q = lambda l: q([x for x in l[1:] if x <= l[0]]) + [l[0]] + q([x for x in l[1:] if x >= l[0]]) if l else []
print(q(d))