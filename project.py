from _collections_abc import Iterable

l = [[1, 'a', ['cat', ["dog2"]], 2], [[[3]], 'dog'], 4, 5]
l2 = [[1, 2], [3, 4], [5, 6, 7]]


def flattenList(lis):
    flat_list = []
    for sublist in lis:
        if isinstance(sublist, Iterable) and not isinstance(sublist, str):
            for deeperSublist in sublist:
                if isinstance(deeperSublist, Iterable) and not isinstance(deeperSublist, str):
                    for items in deeperSublist:
                        if isinstance(items, Iterable) and not isinstance(items, str):
                            for lastItem in items:
                                if isinstance(lastItem, Iterable) and not isinstance(lastItem, str):
                                    flat_list.append(lastItem)
                                else:
                                    flat_list.append(lastItem)
                        else:
                            flat_list.append(items)
                else:
                    flat_list.append(deeperSublist)
        else:
            flat_list.append(sublist)
    return flat_list


def reverseList(lis):
    new_list = []
    for sublist in lis:
        if isinstance(sublist, Iterable):
            reversed_list = sublist[::-1]
            new_list.append(reversed_list)
        else:
            new_list.append(sublist[::-1])
    return new_list[::-1]


print(flattenList(l))
print(reverseList(l2))