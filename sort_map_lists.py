def merge(list1, list2):
	return [*sorted(map(int, list1 + list2))]

list1, list2 = input().split(), input().split()

print(merge(list1, list2))