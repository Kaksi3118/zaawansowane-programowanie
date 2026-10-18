def adding_lists(list_a: list, list_b: list) -> list:
    for i in range(len(list_a)):
        if list_b[i] not in list_a:
            list_a.append(list_b[i])
    for i in range(len(list_a)):
        list_a[i] = list_a[i] ** 3
    return list_a 

print(adding_lists([1, 2, 3], [1, 3, 4]))
